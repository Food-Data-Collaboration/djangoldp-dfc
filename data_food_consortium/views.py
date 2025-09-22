import logging
import validators
from enum import StrEnum
from urllib.parse import urlparse

from django.conf import settings
from django.shortcuts import render
from django.urls.resolvers import get_resolver

from rest_framework.response import Response
from rest_framework.views import APIView
from djangoldp.filters import SearchByQueryParamFilterBackend
from djangoldp.models import Model
from djangoldp.views.ldp_viewset import LDPViewSet
from djangoldp.views.webid import InstanceWebIDView
from djangoldp_csv.errors import FieldParsingError
from djangoldp_csv.views import BaseCSVImportView

from data_food_consortium.forms import EnterpriseImportForm
from data_food_consortium.proxy.keycloak import KeycloakResourceServerAuthentication
from data_food_consortium.proxy.resource import ProxyRefreshParser, ResourceServerClient
from data_food_consortium.serializers import EnterpriseSerializer


logger = logging.getLogger("djangoldp")


class WebhookEventType(StrEnum):
    UPDATE = "update"
    REFRESH = "refresh"
    REVOKE = "revoke"


class CacheWebhookView(APIView):
    """
    An endpoint which accepts POST requests from a data source directing cache refreshes on the existing data.
    """

    authentication_classes = [KeycloakResourceServerAuthentication]

    def process(self, request, data):
        if data["eventType"] == WebhookEventType.UPDATE:
            # Parse and import the graph.
            # TODO: trigger optional behaviour in the parser to fail loudly.
            ProxyRefreshParser(data["@id"]).parse(data)
        elif data["eventType"] == WebhookEventType.REFRESH:
            host = urlparse(request.platform_urlid)
            ResourceServerClient(f"{host.scheme}://{host.netloc}/").request_scope(
                data["scope"]
            )
        elif data["eventType"] == WebhookEventType.REVOKE:
            for obj in data["objects"]:
                Model.get_subclass_with_rdf_type(obj["@type"]).objects.filter(
                    proxy_of=obj["@id"]
                ).delete()

    def post(self, request, *args, **kwargs):
        data = request.data
        # TODO: respond 403 id the keycloak token is valid, but doesn't correspond to the host of the resource given in @id

        try:
            WebhookEventType(data["eventType"])
        except KeyError:
            return Response({"error": "No event type given"}, status=400)
        except ValueError:
            return Response({"error": "Unrecognised event type"}, status=400)

        # Cleaning webhook POST data.
        if data["eventType"] == WebhookEventType.REFRESH:
            if "enterpriseUrlid" not in data:
                return Response(
                    {"error": "enterpriseUrlid is a required parameter"}, status=400
                )
            if "scope" not in data:
                return Response({"error": "scope is a required parameter"}, status=400)
            if validators.url(data["scope"]):
                data["scope"] = data["scope"].split("#")[-1]
            if data["scope"] not in settings.DFC_KEYCLOAK_READ_SCOPES:
                return Response({"error": "Scope not recognised"}, 400)
        elif data["eventType"] == WebhookEventType.REVOKE:
            if "objects" not in data or not len(data["objects"]):
                return Response({"error": "No objects given to revoke"}, status=400)
            for obj in data["objects"]:
                if len({"@id", "@type"}.difference(set(obj.keys()))):
                    return Response(
                        {
                            "error": "Objects should be serialised with only @id and @type"
                        },
                        status=400,
                    )

        self.process(request, data)
        return Response({}, status=200)


class EnterpriseImportView(BaseCSVImportView):
    def get_form_class(self, *args, **kwargs):
        return EnterpriseImportForm(*args, **kwargs)

    def render_import(self, request, form, success=False):
        return render(
            request, "enterprise_import.html", {"form": form, "success": success}
        )

    def get(self, request, *args, **kwargs):
        return self.render_import(request, self.get_form_class())

    def post(self, request, *args, **kwargs):
        form = self.get_form_class(request.POST, request.FILES)
        if not form.is_valid():
            return self.render_import(request, form)

        try:
            self.process_form(form)
        except FieldParsingError:
            return self.render_import(request, form)

        return self.render_import(request, form, success=True)


class EnterpriseViewset(LDPViewSet):
    filter_backends = [SearchByQueryParamFilterBackend]
    serializer_class = EnterpriseSerializer

    def get_serializer_class(self):
        model_name = self.model._meta.object_name.lower()
        try:
            lookup_field = get_resolver().reverse_dict[model_name + "-detail"][0][0][1][
                0
            ]
        except:
            lookup_field = "urlid"

        meta_args = {
            "model": self.model,
            "extra_kwargs": {"@id": {"lookup_field": lookup_field}},
            "depth": self.get_depth(),
            "extra_fields": self.nested_fields + ["dropoff_points"],
        }

        if self.fields:
            meta_args["fields"] = self.fields
        else:
            meta_args["exclude"] = self.exclude or getattr(
                self.model._meta, "serializer_fields_exclude", ()
            )
        # create the Meta class to associate to LDPSerializer, using meta_args param

        from djangoldp.serializers import LDPSerializer

        if self.serializer_class is None:
            self.serializer_class = LDPSerializer

        parent_meta = (
            (self.serializer_class.Meta,)
            if hasattr(self.serializer_class, "Meta")
            else ()
        )
        meta_class = type("Meta", parent_meta, meta_args)

        return type(self.serializer_class)(
            self.model._meta.object_name.lower() + "Serializer",
            (self.serializer_class,),
            {"Meta": meta_class},
        )


class PersonViewset(LDPViewSet):
    filter_backends = [SearchByQueryParamFilterBackend]


class SuppliedProductViewset(LDPViewSet):
    filter_backends = [SearchByQueryParamFilterBackend]


class ProxyWebIDView(InstanceWebIDView):
    def get_profile_data(self, request):
        profile_data = super().get_profile_data(request)
        profile_data["dfc-t:requestedScopes"] = (
            "https://cdn.startinblox.com/owl/dfc/taxonomies/cqcm.jsonld"
        )
        return profile_data
