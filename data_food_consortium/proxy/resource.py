import logging
import requests

from django.conf import settings
from django.utils import timezone
from rdflib import Graph, URIRef
from rdflib.exceptions import ParserError

from djangoldp.models import Model
from djangoldp.serializers import LDPSerializer

from data_food_consortium.proxy.keycloak import (
    KeycloakAuthenticationException,
    KeycloakClient,
)


RDF_TYPE_PREDICATE = URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#type")


logger = logging.getLogger(__name__)


class ProxyRefreshParser:
    """
    Responsible for parsing an RDF-graph containing data to be proxied by a DjangoLDP application.
    """

    raw_data = None
    graph = None
    data_server_source = ""

    def __init__(self, raw_data, data_server_source):
        self.raw_data = raw_data
        self.graph = Graph()
        self.graph.parse(data=raw_data, format="json-ld")
        self.data_server_source = data_server_source

    def get_serializer_class(self, model, depth=2):
        # NOTE: LDPSerializer cannot be used without meta args:
        #   https://git.startinblox.com/djangoldp-packages/djangoldp/-/issues/277
        meta_args = {
            "model": model,
            "depth": depth,
            "fields": "__all__",
        }
        meta_class = type("Meta", (), meta_args)
        return type(LDPSerializer)(
            "LDPSerializer", (LDPSerializer,), {"Meta": meta_class}
        )

    def parse(self):
        import_started_at = timezone.now()
        subjects = set(self.graph.subjects())

        for subject in subjects:
            # Ensure that the subject is not a blank node.
            # TODO: allow blank nodes, but transfer their urlid to a global one
            if not isinstance(subject, URIRef):
                logger.error(f"ERR came across blank node in the input: {subject}")
                continue

            # Evaluate the @type and find a corresponding model that we can store.
            resolved_model = None
            model_types = []
            resolved_type_uri = None
            for type_uri in self.graph.objects(subject, RDF_TYPE_PREDICATE):
                try:
                    model_types += [str(type_uri), self.graph.qname(type_uri)]
                except (ValueError, KeyError) as e:
                    logger.warn(
                        f"Unable to use compacted form of {type_uri}. RDFLib error: {e}"
                    )

            for type_uri in model_types:
                resolved_model = Model.get_subclass_with_rdf_type(type_uri)
                if resolved_model is not None:
                    resolved_type_uri = type_uri
                    break

            if resolved_model is None:
                logger.error(
                    f"ERR could not resolve a model with configured type_uri {model_types}"
                )
                continue

            # Parsing the graph into serializable data for our model
            resource_data = {
                "@type": resolved_type_uri,
            }
            for pred, obj in self.graph.predicate_objects(subject):
                if pred == RDF_TYPE_PREDICATE:
                    continue

                # Handle both URIs and literals
                value = str(obj) if isinstance(obj, URIRef) else obj.toPython()
                resource_data[str(pred)] = value

                # Create a copy so that we can tolerate compacted and expanded forms
                # LDPSerializer will ignore non-mapped values later
                try:
                    resource_data[self.graph.qname(pred)] = value
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

            # Map the RDF types to local model names where possible, and resolve foreign keys
            for field in resolved_model._meta._get_fields(forward=True, reverse=True):
                field_path = f"{resolved_model}.{field.name}"
                rdf_type = None

                # Prioritise related RDF type on a relation
                if field.remote_field is not None and hasattr(
                    field.remote_field, "related_rdf_type"
                ):
                    rdf_type = field.remote_field.related_rdf_type
                # Otherwise the field must have an RDF type configured to be considered
                elif not hasattr(field, "rdf_type"):
                    logger.warn(
                        f"Skipping field import {field_path} because it lacks rdf_type"
                    )
                    continue
                else:
                    rdf_type = field.rdf_type

                if rdf_type not in resource_data:
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

                    related_instance_urlid = resource_data.pop(rdf_type)
                    related_instance = field.related_model.objects.filter(
                        urlid=related_instance_urlid
                    ).first()
                    existing_data = {}

                    if related_instance is not None:
                        serializer_class = self.get_serializer_class(
                            field.related_model
                        )
                        existing_data = serializer_class(related_instance).data

                    if field.one_to_many or field.many_to_many:
                        # TODO: related_instance_urlid may not be a single value, since this is a many field
                        resource_data[field.name] = {
                            "ldp:contains": [
                                {
                                    "@id": related_instance_urlid,
                                    field.field.name: {"@id": instance.urlid},
                                }
                                | existing_data
                            ]
                        }
                    else:
                        resource_data[field.name] = {
                            "@id": related_instance_urlid
                        } | existing_data
                else:
                    resource_data[field.name] = resource_data.pop(rdf_type)

            # Use LDPSerializer with the resolved model to save it in our database.
            logger.debug(f"\nCOMMITTING SAVE: {resource_data}")

            serializer_class = self.get_serializer_class(resolved_model, 10)
            serializer = serializer_class(instance, data=resource_data)
            serializer.is_valid(raise_exception=True)
            instance = serializer.save()

            # Attempt to remove any implicitly deleted data (data previously returned on this endpoint now missing).
            deleted = resolved_model.objects.filter(
                updated_at__lt=import_started_at,
                data_server_source=self.data_server_source,
            ).delete()
            logger.info(
                f"Deleted {deleted} instances of {resolved_model} during cleanup on data source {self.data_server_source}"
            )


class ResourceServerClient:
    """
    Manages the proxy's connection to a data source, authenticated with Keycloak.
    """

    dataserver_url = ""

    def __init__(self, dataserver_url):
        self.dataserver_url = dataserver_url

    def request_all_scopes(self):
        for scope in settings.DFC_KEYCLOAK_READ_SCOPES:
            try:
                self.request_scope(scope)
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

    def _request_and_process_scope_at_endpoint(self, scope: str, endpoint: str):
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
        ProxyRefreshParser(data, endpoint).parse()

        if "next" in data and data["next"] is not None:
            self._request_and_process_scope_at_endpoint(scope, data["next"])

    def request_scope(self, scope: str):
        """
        Discovers the appropriate endpoint for a scope, and then processes it.

        :raises KeycloakAuthenticationException: if authentication with Keycloak is unsuccessful
        :raises RequestException: if dataserver request is unsuccessful
        """
        # Each scope has an associated endpoint.
        # TODO: Complete endpoint discovery at /.well-known/dfc/
        endpoint = f"{self.dataserver_url}{settings.DFC_KEYCLOAK_READ_SCOPES[scope]}"
        self._request_and_process_scope_at_endpoint(scope, endpoint)
