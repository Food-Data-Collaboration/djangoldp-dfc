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
    platform_urlid = None
    data = None

    def __init__(self, platform_urlid, data):
        self.platform_urlid = platform_urlid
        self.data = data

    def process_update(self):
        # Parse and import the graph.
        # TODO: trigger optional behaviour in the parser to fail loudly.
        parser = ProxyRefreshParser(self.data["@id"])
        parser.parse(self.data)
        if settings.DFC_STORE_IMPORT_REPORTS:
            parser.create_record(ResourceImportSource.UPDATE_WEBHOOK)

    def process_refresh(self):
        host = urlparse(self.platform_urlid)
        ResourceServerClient(f"{host.scheme}://{host.netloc}/").request_scope(
            self.data["scope"], ResourceImportSource.REFRESH_WEBHOOK
        )

    def process_revoke(self, source):
        for obj in self.data["objects"]:
            Model.get_subclass_with_rdf_type(obj["@type"]).objects.filter(
                proxy_of=obj["@id"]
            ).delete()
        if settings.DFC_STORE_IMPORT_REPORTS:
            RevokeWebhookRecord.objects.create(
                data=self.data, platform_urlid=self.platform_urlid, source=source
            )

    def process(self, source: WebhookEventSource = WebhookEventSource.DATASERVER):
        if self.data["eventType"] == WebhookEventType.UPDATE:
            self.process_update()
        elif self.data["eventType"] == WebhookEventType.REFRESH:
            self.process_refresh()
        elif self.data["eventType"] == WebhookEventType.REVOKE:
            self.process_revoke(source)
