from enum import StrEnum
from urllib.parse import urlparse

from django.conf import settings
from djangoldp.models import Model

from data_food_consortium.enums import ResourceImportSource, WebhookEventSource
from data_food_consortium.models import RevokeWebhookRecord
from data_food_consortium.proxy.resource import ProxyRefreshParser, ResourceServerClient


class WebhookEventType(StrEnum):
    UPDATE = "update"
    REFRESH = "refresh"
    REVOKE = "revoke"


class WebhookProcessor:
    data_server = None
    data = None

    def __init__(self, data_server, data):
        self.data_server = data_server
        self.data = data

    def process_update(self):
        # Parse and import the graph.
        # TODO: trigger optional behaviour in the parser to fail loudly.
        ProxyRefreshParser(self.data["@id"], ResourceImportSource.UPDATE_WEBHOOK).parse(
            self.data
        )

    def process_refresh(self):
        host = urlparse(self.data_server.urlid)
        ResourceServerClient(
            f"{host.scheme}://{host.netloc}/", ResourceImportSource.REFRESH_WEBHOOK
        ).request_scope(self.data["scope"])

    def process_revoke(self, source):
        for obj in self.data["objects"]:
            Model.get_subclass_with_rdf_type(obj["@type"]).objects.filter(
                proxy_of=obj["@id"]
            ).delete()
        if settings.DFC_STORE_IMPORT_REPORTS:
            RevokeWebhookRecord.objects.create(
                data=self.data, data_server=self.data_server, source=source
            )

    def process(self, source: WebhookEventSource = WebhookEventSource.DATASERVER):
        if self.data["eventType"] == WebhookEventType.UPDATE:
            self.process_update()
        elif self.data["eventType"] == WebhookEventType.REFRESH:
            self.process_refresh()
        elif self.data["eventType"] == WebhookEventType.REVOKE:
            self.process_revoke(source)
