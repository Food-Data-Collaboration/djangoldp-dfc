import logging
import requests

from django.conf import settings
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

    def request_scope(self, scope: str):
        """
        Requests an access token from Keycloak for a given scope, and then requests from the dataserver the associated endpoint.

        :raises KeycloakAuthenticationException: if authentication with Keycloak is unsuccessful
        :raises RequestException: if dataserver request is unsuccessful
        """
        token = KeycloakClient(scope).get_access_token()

        # Each scope has an associated endpoint
        headers = {"Authorization": f"Bearer {token}"}
        endpoint = f"{self.dataserver_url}{settings.DFC_KEYCLOAK_READ_SCOPES[scope]}"
        response = requests.get(endpoint, headers=headers)
        response.raise_for_status()
        data = response.json()

        # Parse the returned graph, resolve and import to the relevant models.
        g = Graph()
        g.parse(data=data, format="json-ld")
        logger.info(f"\n\nEndpoint: {scope}")
        subjects = set(g.subjects())

        for subject in subjects:
            # Ensure that the subject is not a blank node.
            # TODO: allow blank nodes, but transfer their urlid to a global one
            if not isinstance(subject, URIRef):
                logger.error(f"ERR came across blank node in the input: {subject}")
                continue

            # Evaluate the @type and find a corresponding model that we can store.
            resolved_model = None
            model_types = [
                str(type_uri) for type_uri in g.objects(subject, RDF_TYPE_PREDICATE)
            ]
            resolved_type_uri = None

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
            resource_data = {"@id": str(subject), "@type": resolved_type_uri}
            for pred, obj in g.predicate_objects(subject):
                if pred == RDF_TYPE_PREDICATE:
                    continue

                # Handle both URIs and literals
                value = str(obj) if isinstance(obj, URIRef) else obj.toPython()
                resource_data[str(pred)] = value

            # Map the RDF types to local model names where possible, and resolve foreign keys
            for field in resolved_model._meta._get_fields(forward=True, reverse=True):
                field_path = f"{resolved_model}.{field.name}"

                if not hasattr(field, "rdf_type"):
                    if field.remote_field is None:
                        logger.debug(
                            f"Skipping field import {field_path} because it lacks rdf_type"
                        )
                        continue
                    # TODO: related_rdf_type?
                    if not hasattr(field.remote_field, "rdf_type"):
                        logger.debug(
                            f"Skipping field import {field_path} because remote_field {field.remote_field.name} lacks rdf_type"
                        )
                        continue
                    field.rdf_type = field.remote_field.rdf_type

                if field.rdf_type not in resource_data:
                    logger.debug(
                        f"Skipping field import {field_path} because {field.rdf_type} is not present in data"
                    )
                    continue

                # Foreign Keys
                if field.related_model is not None:
                    if field.related_model._meta.abstract:
                        logger.debug(
                            f"Skipping field import {field_path} because the related model ({field.related_model}) is abstract"
                        )
                        continue

                    instance_urlid = resource_data.pop(field.rdf_type)
                    instance = field.related_model.objects.filter(
                        urlid=instance_urlid
                    ).first()
                    existing_data = {}

                    if instance is not None:
                        # NOTE: LDPSerializer cannot be used without meta args:
                        #   https://git.startinblox.com/djangoldp-packages/djangoldp/-/issues/277
                        meta_args = {
                            "model": field.related_model,
                            "depth": 2,
                            "fields": "__all__",
                        }
                        meta_class = type("Meta", (), meta_args)
                        serializer_class = type(LDPSerializer)(
                            "LDPSerializer", (LDPSerializer,), {"Meta": meta_class}
                        )
                        existing_data = serializer_class(instance).data

                    if field.one_to_many or field.many_to_many:
                        # TODO: instance_urlid may not be a single value, since this is a many field
                        resource_data[field.name] = {
                            "ldp:contains": [
                                {
                                    "@id": instance_urlid,
                                    field.field.name: {"@id": resource_data["@id"]},
                                }
                                | existing_data
                            ]
                        }
                    else:
                        resource_data[field.name] = {
                            "@id": instance_urlid
                        } | existing_data
                else:
                    resource_data[field.name] = resource_data.pop(field.rdf_type)

            # Use LDPSerializer with the resolved model to save it in our database.
            logger.debug("\nCOMMITTING SAVE")
            logger.debug(str(resource_data))
            instance = resolved_model.objects.filter(urlid=resource_data["@id"]).first()

            # NOTE: LDPSerializer cannot be used without meta args:
            #   https://git.startinblox.com/djangoldp-packages/djangoldp/-/issues/277
            meta_args = {
                "model": resolved_model,
                "depth": 10,
                "fields": "__all__",
            }
            meta_class = type("Meta", (), meta_args)
            serializer_class = type(LDPSerializer)(
                "LDPSerializer", (LDPSerializer,), {"Meta": meta_class}
            )
            serializer = serializer_class(instance, data=resource_data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
