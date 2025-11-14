import logging
import requests
import urllib
import uuid

from django.conf import settings
from django.db.models import Q
from django.utils import timezone
from rdflib import BNode, Graph, URIRef
from rdflib.exceptions import ParserError

from djangoldp import fields
from djangoldp.models import Model
from djangoldp.serializers import LDPSerializer

from data_food_consortium.enums import ResourceImportSource
from data_food_consortium.models import ResourceImportRecord
from data_food_consortium.proxy.keycloak import (
    KeycloakAuthenticationException,
    KeycloakClient,
)


RDF_TYPE_PREDICATE = URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#type")
SCOPES_BASE_URI = "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/scopes.rdf#"


logger = logging.getLogger(__name__)


class ProxyRefreshParser:
    """
    Responsible for parsing an RDF-graph containing data to be proxied by a DjangoLDP application.
    """

    data_server_source = ""
    import_started_at = None
    imported_models = None
    imported_subjects = None
    deleted_subjects = None
    data_batches = None

    _dfc_v1_container_properties = [
        "dfc-b:manages",
        "dfc-b:supplies",
        "dfc-b:hasAddress",
        "dfc-b:hasSocialMedia",
        "dfc-b:referencedBy",
        "dfc-b:offeredThrough",
        "dfc-b:affiliatedTo",
        "dfc-b:hasReference",
        "dfc-b:defines",
        "dfc-b:offers",
        "dfc-b:priceOf",
        "dfc-b:mainContactOf",
        "dfc-b:coordinatedBy",
        "dfc-b:hasObject",
        "dfc-b:hosts",
        "cqcm:services",
        "cqcm:suppliers",
        "cqcm:shippingOptions",
        "dfc-b:hasOption",
        "dfc-b:deliveries",
        "dfc-b:collections",
    ]

    def __init__(self, data_server_source):
        dss = urllib.parse.urlparse(data_server_source)
        self.data_server_source = f"{dss.scheme}://{dss.netloc}"
        self.import_started_at = timezone.now()
        self.imported_models = set()
        self.imported_subjects = list()
        self.deleted_subjects = list()
        self.data_batches = list()

    def _cache_data_batch(self, data):
        self.data_batches.append(data)

    def get_serializer_class(self, model, depth=2, extra_fields=[]):
        try:
            serializer_class = model.serializer_class()
        except AttributeError:
            serializer_class = LDPSerializer

        # NOTE: LDPSerializer cannot be used without meta args:
        #   https://git.startinblox.com/djangoldp-packages/djangoldp/-/issues/277
        meta_args = {
            "model": model,
            "depth": depth,
            "fields": "__all__",
            "extra_fields": extra_fields,
        }
        meta_class = type("Meta", (), meta_args)
        return type(serializer_class)(
            serializer_class.__class__.__name__,
            (serializer_class,),
            {"Meta": meta_class},
        )

    def resolve_model_for_subject(self, graph, subject):
        """Discovers a DjangoLDP model for a given RDF subject."""
        model_types = []
        for type_uri in graph.objects(subject, RDF_TYPE_PREDICATE):
            try:
                model_types += [str(type_uri), graph.qname(type_uri)]
            except (ValueError, KeyError) as e:
                logger.warn(
                    f"Unable to use compacted form of {type_uri}. RDFLib error: {e}"
                )

        for type_uri in model_types:
            resolved_model = Model.get_subclass_with_rdf_type(type_uri)
            if resolved_model is not None:
                return resolved_model, type_uri

        # Unable to resolve model, log error if necessary.
        if set(model_types) != {
            "http://www.w3.org/ns/ldp#Container",
            "ldp:Container",
        }:
            logger.warn(
                f"Unable to resolve a model with configured type_uri {model_types}."
                "If this is a container or a sequence, it is not a problem."
            )

        return None, None

    def reformat_list_to_container(self, key, jsonld_data):
        if isinstance(jsonld_data, str):
            container = [{"@id": jsonld_data}]
        elif isinstance(jsonld_data, list):
            container = [
                {"@id": x}
                for x in jsonld_data
                if type(x) is not dict or ("@id" not in x and "@context" not in x)
            ]
        elif isinstance(jsonld_data, dict):
            return jsonld_data
        else:
            logger.error(
                f"Unexpected value for property {key} ({type(jsonld_data)}). {jsonld_data}"
            )
            return jsonld_data
        return {
            "@id": f"_:generated-container-{uuid.uuid4()}",
            "@type": "ldp:Container",
            "ldp:contains": container,
        }

    def transform_dfc_v1(self, jsonld_data):
        """
        DFC v1 does not require data-servers to send us their data in containers,
        which causes problems with RDFLib's graph parser and DjangoLDP's serializer.
        Our workaround is to transform the lists of string IDs we receive into proper
        containers.

        This is achieved with implicit knowledge of the DFC fields, and a recursive search of
        the data received.
        """
        if isinstance(jsonld_data, list):
            for i, ele in enumerate(jsonld_data):
                jsonld_data[i] = self.transform_dfc_v1(ele)
        elif isinstance(jsonld_data, dict):
            for key in jsonld_data.keys():
                if key in self._dfc_v1_container_properties:
                    jsonld_data[key] = self.reformat_list_to_container(
                        key, jsonld_data[key]
                    )
                else:
                    jsonld_data[key] = self.transform_dfc_v1(jsonld_data[key])

        return jsonld_data

    def parse(self, jsonld_data):
        jsonld_data = self.transform_dfc_v1(jsonld_data)

        graph = Graph()
        graph.parse(data=jsonld_data, format="json-ld")
        subjects = set(graph.subjects())

        for subject in subjects:
            resolved_model, resolved_type_uri = self.resolve_model_for_subject(
                graph, subject
            )
            if resolved_model is None:
                continue

            # Parsing the graph into serializable data for our model
            resource_data = {
                "@type": resolved_type_uri,
                "data_server_source": self.data_server_source,
                "proxy_of": str(subject),
                "allow_create_backlink": False,
            }
            source_data = {}
            for pred, obj in graph.predicate_objects(subject):
                if pred == RDF_TYPE_PREDICATE:
                    continue

                # Map RDF values to Python values.
                if isinstance(obj, BNode):
                    # Blank nodes serialized into JSON.
                    value = {p: o for p, o in graph.predicate_objects(obj)}
                elif isinstance(obj, URIRef):
                    value = str(obj)
                else:
                    value = obj.toPython()
                source_data[str(pred)] = value

                # Create a copy so that we can tolerate compacted and expanded forms
                # LDPSerializer will ignore non-mapped values later
                try:
                    source_data[graph.qname(pred)] = value
                except (ValueError, KeyError) as e:
                    logger.warn(
                        f"Unable to use compacted form of {pred}. RDFLib error: {e}"
                    )

            # Resolve a local instance of the model, so that we know the urlid
            instance = resolved_model.objects.filter(proxy_of=str(subject)).first()
            if instance is None:
                # Must set urlid before
                instance = resolved_model.objects.create(
                    proxy_of=str(subject),
                    data_server_source=self.data_server_source,
                    allow_create_backlink=False,
                )
            self.imported_models.add(resolved_model)
            self.imported_subjects.append(instance.proxy_of)

            # Map the RDF types to local model names where possible, and resolve foreign keys
            serialize_fields_extra = []
            json_fields = {}
            for field in resolved_model._meta._get_fields(forward=True, reverse=True):
                field_path = f"{resolved_model}.{field.name}"
                rdf_type = None

                # Prioritise related RDF type on a relation
                if field.remote_field is not None and hasattr(
                    field.remote_field, "related_rdf_type"
                ):
                    rdf_type = field.remote_field.related_rdf_type
                # Otherwise the field must have an RDF type configured to be considered
                elif not hasattr(field, "rdf_type") or field.rdf_type is None:
                    logger.warn(
                        f"Skipping field import {field_path} because it lacks rdf_type"
                    )
                    continue
                else:
                    rdf_type = field.rdf_type

                # Attempt to fall back on expanded form, if compacted form is not in the dataset
                try:
                    rdf_type = (
                        graph.namespace_manager.expand_curie(rdf_type)
                        if rdf_type not in source_data
                        else rdf_type
                    )
                except ValueError as e:
                    logger.warn(
                        f"Ignorable while expanding property {rdf_type} on {field_path}"
                    )
                    logger.error(str(e))

                if rdf_type not in source_data:
                    logger.warn(
                        f"Skipping field import {field_path} because {rdf_type} is not present in data"
                    )
                    continue

                # Foreign Keys
                if field.related_model is not None:
                    if field.related_model._meta.abstract:
                        logger.warn(
                            f"Skipping field import {field_path} because the related model ({field.related_model}) is abstract"
                        )
                        continue
                    if field.one_to_many or field.many_to_many:
                        logger.info(
                            f"Many-to-many field expected to be imported later {field_path}"
                        )
                        continue

                    related_instance_urlid = source_data.pop(rdf_type)
                    related_instance = field.related_model.objects.filter(
                        proxy_of=related_instance_urlid
                    ).first()

                    if related_instance is None:
                        related_instance = field.related_model.objects.create(
                            proxy_of=related_instance_urlid
                        )

                    resource_data[field.name] = {
                        "@id": related_instance.urlid,
                        "data_server_source": self.data_server_source,
                        "proxy_of": related_instance_urlid,
                        "allow_create_backlink": False,
                    }
                else:
                    resource_data[field.name] = source_data.pop(rdf_type)

                # Workaround for lack of JSONField support in DjangoLDP.
                if isinstance(field, fields.JSONField):
                    json_fields[field.name] = resource_data[field.name]
                    resource_data.pop(field.name)

                if (
                    hasattr(resolved_model._meta, "serializer_fields")
                    and field.name not in resolved_model._meta.serializer_fields
                ):
                    serialize_fields_extra.append(field.name)

            # Use LDPSerializer with the resolved model to save it in our database.
            serializer_class = self.get_serializer_class(
                resolved_model, 10, serialize_fields_extra
            )
            resource_data["@id"] = instance.urlid
            serializer = serializer_class(instance, data=resource_data)
            serializer.is_valid(raise_exception=True)
            instance = serializer.save()

            # Workaround for lack of JSONField support in DjangoLDP.
            if len(json_fields):
                for field_name in json_fields:
                    setattr(instance, field_name, json_fields[field_name])
                instance.save()

        logger.info(f"Finished importing {len(self.imported_subjects)} subjects")
        self._cache_data_batch(jsonld_data)

    def clean_up(self):
        """
        LDPSerializer creates objects implicitly that in our case become duplicate objects, because of the requirement that
        proxy_of define the original resource, not a urlid (DjangoLDP is not built with proxies in mind).

        Similarly, objects may have been previously cached and sinced removed, either because they were deleted or because
        we no longer have permission to proxy them.

        This method finds and deletes those objects.
        """
        ldp_serializer_created = Q(
            urlid__startswith=self.data_server_source, proxy_of__isnull=True
        )
        missing_from_new_import = Q(
            updated_at__lt=self.import_started_at,
            data_server_source__startswith=self.data_server_source,
        )

        for imported_model in self.imported_models:
            deleted = imported_model.objects.filter(
                ldp_serializer_created | missing_from_new_import
            )
            self.deleted_subjects += [d.proxy_of for d in deleted]
            deleted.delete()
            logger.info(
                f"Deleted {deleted} instances of {imported_model} during cleanup on data source {self.data_server_source}"
            )

    def create_record(self, source: ResourceImportSource):
        self.imported_subjects.sort()
        ResourceImportRecord.objects.create(
            import_started_at=self.import_started_at,
            data_batches=self.data_batches,
            data_server_source=self.data_server_source,
            imported_models="\n".join([str(m) for m in self.imported_models]),
            imported_subjects="\n".join(self.imported_subjects),
            deleted_subjects="\n".join(self.deleted_subjects),
            source=source,
        )
        logger.info(f"Import finished at {timezone.now()}. Report created in database")


class ResourceServerClient:
    """
    Manages the proxy's connection to a data source, authenticated with Keycloak.
    """

    dataserver_url = ""
    scope_config = None

    def __init__(self, dataserver_url):
        self.dataserver_url = dataserver_url
        self.scope_config = settings.DFC_KEYCLOAK_READ_SCOPES.copy()

        discovery_endpoint = f"{dataserver_url}.well-known/dfc/"
        response = requests.get(discovery_endpoint)
        if response.status_code == 200:
            data_server_endpoints = response.json()
            for scope in settings.DFC_KEYCLOAK_READ_SCOPES:
                key = f"{SCOPES_BASE_URI}{scope}"
                if key in data_server_endpoints:
                    val = data_server_endpoints[key]
                    if val.startswith("/"):
                        val = val[1:]
                    self.scope_config[scope] = val
            logger.debug(
                f"Configured ResourceServerClient with discovered config {self.scope_config}"
            )
        else:
            logger.warn(
                "Configured ResourceServerClient with default config, "
                f"discovery endpoint {discovery_endpoint} responded {response.status_code}"
            )

    def request_all_scopes(self, source: ResourceImportSource):
        for scope in settings.DFC_KEYCLOAK_READ_SCOPES:
            try:
                self.request_scope(scope, source)
            except KeycloakAuthenticationException as e:
                msg = f"ERR authenticating dataserver {self.dataserver_url} with Keycloak, while requesting {scope}"
                logger.error(msg)
                logger.error(str(e))
            except requests.exceptions.RequestException as e:
                msg = f"ERR requesting a scope {scope} from dataserver {self.dataserver_url}"
                logger.error(msg)
                logger.error(str(e))
            except (ParserError, ValueError, TypeError) as e:
                msg = f"ERR parsing response from dataserver {self.dataserver_url} on scope {scope}"
                logger.error(msg)
                logger.error(str(e))

    def _get_auth_headers_with_token_for_scope(self, scope: str):
        token = KeycloakClient(scope).get_access_token()
        return {"Authorization": f"Bearer {token}"}

    def _request_and_process_scope_at_endpoint(self, parser, scope: str, endpoint: str):
        """
        Requests an access token from Keycloak for a given scope,
        and then recursively requests from the dataserver the associated endpoint,
        scraping all available data until complete.
        """
        headers = self._get_auth_headers_with_token_for_scope(scope)
        response = requests.get(endpoint, headers=headers)
        response.raise_for_status()
        data = response.json()

        # Parse the returned graph, resolve and import to the relevant models.
        parser.parse(data)

        # If there is more data, continue.
        if "next" in data and data["next"] is not None:
            self._request_and_process_scope_at_endpoint(parser, scope, data["next"])

    def request_scope(self, scope: str, source: ResourceImportSource):
        """
        Discovers the appropriate endpoint for a scope, and then processes it.

        :raises KeycloakAuthenticationException: if authentication with Keycloak is unsuccessful
        :raises RequestException: if dataserver request is unsuccessful
        """
        # Each scope has an associated endpoint.
        endpoint = f"{self.dataserver_url}{self.scope_config[scope]}"
        parser = ProxyRefreshParser(endpoint)
        self._request_and_process_scope_at_endpoint(parser, scope, endpoint)
        parser.clean_up()
        if settings.DFC_STORE_IMPORT_REPORTS:
            parser.create_record(source)
