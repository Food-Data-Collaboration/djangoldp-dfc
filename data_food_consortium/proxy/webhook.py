from enum import StrEnum
from urllib.parse import urlparse

from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import transaction
from djangoldp.models import Model

from data_food_consortium.auth_utils import normalise_to_domain
from data_food_consortium.enums import ResourceImportSource, WebhookEventSource
from data_food_consortium.models import GrantWebhookRecord, RevokeWebhookRecord
from data_food_consortium.models_common import Platform
from data_food_consortium.models_permissioning import AssignedScope
from data_food_consortium.proxy.errors import ResourceAnnexationError
from data_food_consortium.proxy.resource import ProxyRefreshParser, ResourceServerClient


class WebhookEventType(StrEnum):
    GRANT = "grant"
    UPDATE = "update"
    REFRESH = "refresh"
    REVOKE = "revoke"


class WebhookProcessor:
    """
    :raises ResourceAnnexationError: if given webhook data references a resource from an external domain
    """

    data_server = None
    data = None

    def __init__(self, data_server, data):
        self.data_server = data_server
        self.data = data

    def _process_grant(self, model, field_name, proxied_obj_urlid):
        """
        :param model: either server's user model or Platform. Must have urlid field.
        :param field_name: corresponds both to webhook data key and to field on AssignedScope. 'platform' or 'user'.
        """
        subject = model.objects.get_or_create(urlid=self.data[field_name])[0]
        scope_kwargs = {
            "data_server": self.data_server,
            field_name: subject,
            "proxied_obj_urlid": proxied_obj_urlid,
        }
        # Delete pre-existing scopes.
        AssignedScope.objects.filter(**scope_kwargs).delete()

        # Create new scopes.
        for scope in self.data["scopes"]:
            scope_kwargs["scope"] = scope
            instance = AssignedScope(**scope_kwargs)
            instance.save()

    def process_grant(self, source):
        for obj in self.data["objects"]:
            if not self.data_server.resource_within_domain(obj["@id"]):
                raise ResourceAnnexationError()

        with transaction.atomic():
            if "platform" in self.data:
                self.data["platform"] = normalise_to_domain(self.data["platform"])
                for obj in self.data["objects"]:
                    self._process_grant(Platform, "platform", obj["@id"])
            if "user" in self.data and settings.DFC_USER_GRANTS_ENABLED:
                for obj in self.data["objects"]:
                    self._process_grant(get_user_model(), "user", obj["@id"])

        if settings.DFC_STORE_IMPORT_REPORTS:
            GrantWebhookRecord.objects.create(
                data=self.data, data_server=self.data_server, source=source
            )

    def process_update(self):
        # Parse and import the graph.
        # TODO: trigger optional behaviour in the parser to fail loudly.
        ProxyRefreshParser(
            self.data_server.urlid, ResourceImportSource.UPDATE_WEBHOOK
        ).parse(self.data)

    def process_refresh(self):
        host = urlparse(self.data_server.urlid)
        ResourceServerClient(
            f"{host.scheme}://{host.netloc}/", ResourceImportSource.REFRESH_WEBHOOK
        ).request_scope(self.data["scope"])

    def process_revoke(self, source):
        with transaction.atomic():
            for obj in self.data["objects"]:
                if not self.data_server.resource_within_domain(obj["@id"]):
                    raise ResourceAnnexationError()
                Model.get_subclass_with_rdf_type(obj["@type"]).objects.filter(
                    proxy_of=obj["@id"]
                ).delete()
        if settings.DFC_STORE_IMPORT_REPORTS:
            RevokeWebhookRecord.objects.create(
                data=self.data, data_server=self.data_server, source=source
            )

    def process(self, source: WebhookEventSource = WebhookEventSource.DATASERVER):
        if self.data["eventType"] == WebhookEventType.GRANT:
            self.process_grant(source)
        elif self.data["eventType"] == WebhookEventType.UPDATE:
            self.process_update()
        elif self.data["eventType"] == WebhookEventType.REFRESH:
            self.process_refresh()
        elif self.data["eventType"] == WebhookEventType.REVOKE:
            self.process_revoke(source)
