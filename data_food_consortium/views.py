import logging
from enum import StrEnum

from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from djangoldp.filters import SearchByQueryParamFilterBackend
from djangoldp.models import Model
from djangoldp.views.ldp_viewset import LDPViewSet
from djangoldp_csv.errors import FieldParsingError
from djangoldp_csv.views import BaseCSVImportView

from data_food_consortium.forms import EnterpriseImportForm
from data_food_consortium.proxy.resource import ProxyRefreshParser


logger = logging.getLogger("djangoldp")


class WebhookEventType(StrEnum):
    UPDATE = "update"
    REFRESH = "refresh"  # TODO
    REVOKE = "revoke"


class CacheWebhookView(APIView):
    """
    An endpoint which accepts POST requests from a data source directing cache refreshes on the existing data.
    """

    def process(self, data):
        if data["eventType"] == WebhookEventType.UPDATE:
            # Parse and import the graph.
            # TODO: trigger optional behaviour in the parser to fail loudly.
            ProxyRefreshParser(data, data["@id"]).parse()
        elif data["eventType"] == WebhookEventType.REVOKE:
            for obj in data["objects"]:
                Model.get_subclass_with_rdf_type(obj["@type"]).objects.filter(
                    proxy_of=obj["@id"]
                ).delete()

    def post(self, request, *args, **kwargs):
        # TODO: Keycloak authentication. Respond 401 if the token is invalid.
        data = request.data
        # TODO: respond 403 id the keycloak token is valid, but doesn't correspond to the host of the resource given in @id

        try:
            WebhookEventType(data["eventType"])
        except KeyError:
            return Response({"error": "No event type given"}, status=400)
        except ValueError:
            return Response({"error": "Unrecognised event type"}, status=400)

        if data["eventType"] == WebhookEventType.REVOKE:
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

        self.process(data)
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


class PersonViewset(LDPViewSet):
    filter_backends = [SearchByQueryParamFilterBackend]


class SuppliedProductViewset(LDPViewSet):
    filter_backends = [SearchByQueryParamFilterBackend]
