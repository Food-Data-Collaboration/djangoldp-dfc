import json
from unittest.mock import patch

from django.conf import settings
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from data_food_consortium.models import Enterprise
from data_food_consortium.tests.factories import DataServerFactory, EnterpriseFactory


def auth_platform_side_effect(platform):
    """Returns a side effectfor a patched authenticate method"""

    def set_request_platform(request):
        request.data_server = platform

    return set_request_platform


@patch(
    "data_food_consortium.proxy.keycloak.KeycloakResourceServerAuthentication.authenticate"
)
class TestWebhooks(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.data_server = DataServerFactory()

    def test_update_platform_access_webhook(self, mock_authenticate):
        mock_authenticate.side_effect = auth_platform_side_effect(self.data_server)

        enterprise = EnterpriseFactory(
            data_server_source=self.data_server, name="Original"
        )
        old_description = enterprise.description
        webhook_data = {
            "@context": settings.LDP_RDF_CONTEXT,
            "@id": enterprise.proxy_of,
            "@type": "dfc-b:Organization",
            "eventType": "update",
            "dfc-b:name": "New",
        }
        response = self.client.post(
            reverse("djangoldp-dfc-webhook"),
            data=json.dumps(webhook_data),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)
        mock_authenticate.assert_called_once()
        self.assertEqual(response.data, {})

        enterprise = Enterprise.objects.get()  # No new Enterprise has been created.
        self.assertEqual(enterprise.name, webhook_data["dfc-b:name"])
        # The new serialization of Enterprise replaces the Enterprise entirely.
        self.assertEqual(enterprise.description, old_description)

    def test_revoke_platform_access_webhook(self, mock_authenticate):
        mock_authenticate.side_effect = auth_platform_side_effect(self.data_server)

        enterprise = EnterpriseFactory(data_server_source=self.data_server)
        webhook_data = {
            "@context": settings.LDP_RDF_CONTEXT,
            "eventType": "revoke",
            "objects": [
                {
                    "@id": enterprise.proxy_of,
                    "@type": "dfc-b:Organization",
                }
            ],
        }
        response = self.client.post(
            reverse("djangoldp-dfc-webhook"),
            data=json.dumps(webhook_data),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)
        mock_authenticate.assert_called_once()
        self.assertEqual(response.data, {})
        self.assertEqual(Enterprise.objects.count(), 0)  # object has been deleted.

    def test_webhook_revoke_others_resource(self, mock_authenticate):
        """I cannot revoke a resource for which I am not the data owner"""
        mock_authenticate.side_effect = auth_platform_side_effect(self.data_server)

        enterprise = EnterpriseFactory(
            data_server_source=DataServerFactory(urlid="https://somewherelese.com")
        )
        webhook_data = {
            "@context": settings.LDP_RDF_CONTEXT,
            "eventType": "revoke",
            "objects": [
                {
                    "@id": enterprise.proxy_of,
                    "@type": "dfc-b:Organization",
                }
            ],
        }
        response = self.client.post(
            reverse("djangoldp-dfc-webhook"),
            data=json.dumps(webhook_data),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 403)
        mock_authenticate.assert_called_once()
        self.assertEqual(
            response.data,
            {"error": "You can only modify resources from your own data server"},
        )
        self.assertEqual(Enterprise.objects.count(), 1)  # object has not been deleted.
