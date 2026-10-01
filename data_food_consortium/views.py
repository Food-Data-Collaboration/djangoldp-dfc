import logging

import validators
from django.conf import settings
from django.shortcuts import render
from djangoldp.filters import SearchByQueryParamFilterBackend
from djangoldp.views.ldp_viewset import LDPViewSet
from djangoldp.views.webid import InstanceWebIDView
from djangoldp_csv.errors import FieldParsingError
from djangoldp_csv.views import BaseCSVImportView
from rest_framework.response import Response
from rest_framework.views import APIView

from data_food_consortium.filters import DFCGrantedPermissionsFilterBackend
from data_food_consortium.forms import EnterpriseImportForm
from data_food_consortium.proxy.errors import ResourceAnnexationError
from data_food_consortium.proxy.keycloak import KeycloakResourceServerAuthentication
from data_food_consortium.proxy.webhook import WebhookEventType, WebhookProcessor

logger = logging.getLogger("djangoldp")


class CacheWebhookView(APIView):
    """
    An endpoint which accepts POST requests from a data source directing cache refreshes on the existing data.
    """

    authentication_classes = [KeycloakResourceServerAuthentication]

    def post(self, request, *args, **kwargs):
        data = request.data
        try:
            WebhookEventType(data["eventType"])
        except KeyError:
            return Response({"error": "No event type given"}, status=400)
        except ValueError:
            return Response({"error": "Unrecognised event type"}, status=400)

        if data["eventType"] == WebhookEventType.GRANT:
            if "platform" not in data and "user" not in data:
                return Response(
                    {"error": "either platform or user web-id needed to grant access"},
                    status=400,
                )
            elif "user" in data and not settings.DFC_USER_GRANTS_ENABLED:
                return Response(
                    {
                        "error": "this platform is not configured to grant access to individual users"
                    },
                    status=400,
                )
            if "scopes" not in data:
                return Response({"error": "scopes is a required parameter"}, status=400)
            if "objects" not in data or not len(data["objects"]):
                return Response(
                    {
                        "error": "objects, containing at least one object is required to grant access"
                    },
                    status=400,
                )
        elif data["eventType"] == WebhookEventType.REFRESH:
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

        try:
            WebhookProcessor(request.data_server, data).process()
        except ResourceAnnexationError:
            return Response(
                {"error": "You can only modify resources from your own data server"},
                status=403,
            )
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
    filter_backends = [
        DFCGrantedPermissionsFilterBackend,
        SearchByQueryParamFilterBackend,
    ]


class PersonViewset(LDPViewSet):
    filter_backends = [
        DFCGrantedPermissionsFilterBackend,
        SearchByQueryParamFilterBackend,
    ]


class SuppliedProductViewset(LDPViewSet):
    filter_backends = [
        DFCGrantedPermissionsFilterBackend,
        SearchByQueryParamFilterBackend,
    ]


class ProxyWebIDView(InstanceWebIDView):
    def get_profile_data(self, request):
        profile_data = super().get_profile_data(request)
        profile_data["dfc-t:requestedScopes"] = settings.DFC_REQUESTED_SCOPES_DOCUMENT
        return profile_data
