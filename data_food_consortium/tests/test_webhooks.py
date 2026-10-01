import json
from unittest.mock import patch

from django.conf import settings
from django.test import TestCase, override_settings
from django.urls import reverse
from rest_framework.test import APIClient

from data_food_consortium.enums import PermissioningScope
from data_food_consortium.models import Enterprise
from data_food_consortium.models_permissioning import AssignedScope
from data_food_consortium.tests.factories import (
    DataServerFactory,
    DFCUserFactory,
    EnterpriseFactory,
    PlatformFactory,
)


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

    def setUpExternalUser(self):
        self.user = DFCUserFactory(
            urlid="https://somewhereelse.com/users/1", is_backlink=True
        )

    def test_update_webhook(self, mock_authenticate):
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

    def test_update_webhook_others_resource(self, mock_authenticate):
        """I cannot update a resource for which I am not the data owner"""
        mock_authenticate.side_effect = auth_platform_side_effect(self.data_server)

        enterprise = EnterpriseFactory(
            data_server_source=DataServerFactory(urlid="https://somewhereelse.com"),
            name="Original",
        )
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
        self.assertEqual(response.status_code, 403)
        mock_authenticate.assert_called_once()
        self.assertEqual(
            response.data,
            {"error": "You can only modify resources from your own data server"},
        )

        enterprise = Enterprise.objects.get()  # No new Enterprise has been created.
        self.assertEqual(enterprise.name, "Original")

    def test_revoke_webhook_platform(self, mock_authenticate):
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

    def test_revoke_webhook_others_resource(self, mock_authenticate):
        """I cannot revoke a resource for which I am not the data owner"""
        mock_authenticate.side_effect = auth_platform_side_effect(self.data_server)

        enterprise = EnterpriseFactory(
            data_server_source=DataServerFactory(urlid="https://somewhereelse.com")
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

    def _assert_expected_scopes(self, scopes, platform=None, user=None, count=1):
        for scope in scopes:
            assigned_scopes = AssignedScope.objects.filter(
                data_server=self.data_server, platform=platform, user=user, scope=scope
            )
            self.assertEqual(assigned_scopes.count(), count)

    def test_grant_webhook_subplatform(self, mock_authenticate):
        mock_authenticate.side_effect = auth_platform_side_effect(self.data_server)

        platform = PlatformFactory()
        enterprise = EnterpriseFactory(data_server_source=self.data_server)
        # Add an enterprise which the subject is not granted access to.
        EnterpriseFactory(data_server_source=self.data_server)

        scopes = [
            PermissioningScope.READ_ENTERPRISE,
            PermissioningScope.READ_PRODUCTS,
            PermissioningScope.READ_ORDERS,
        ]
        webhook_data = {
            "@context": settings.LDP_RDF_CONTEXT,
            "eventType": "grant",
            "platform": platform.urlid,
            "scopes": scopes,
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
        # Scopes created.
        self._assert_expected_scopes(scopes, platform=platform)

        # Scopes are not created for enterprises not subject to grant.
        self.assertEqual(
            AssignedScope.objects.exclude(
                proxied_obj_urlid=enterprise.proxy_of
            ).count(),
            0,
        )

        # Re-submitting the webhook does not create duplicate grants.
        response = self.client.post(
            reverse("djangoldp-dfc-webhook"),
            data=json.dumps(webhook_data),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)
        self._assert_expected_scopes(scopes, platform=platform)

        # Re-submitting with empty scopes clears the grants.
        webhook_data["scopes"] = []
        response = self.client.post(
            reverse("djangoldp-dfc-webhook"),
            data=json.dumps(webhook_data),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)
        self._assert_expected_scopes(scopes, platform=platform, count=0)

    @override_settings(DFC_USER_GRANTS_ENABLED=True)
    def test_grant_webhook_user(self, mock_authenticate):
        mock_authenticate.side_effect = auth_platform_side_effect(self.data_server)

        self.setUpExternalUser()
        enterprise = EnterpriseFactory(data_server_source=self.data_server)
        # Add an enterprise which the subject is not granted access to.
        EnterpriseFactory(data_server_source=self.data_server)

        scopes = [
            PermissioningScope.READ_ENTERPRISE,
            PermissioningScope.READ_PRODUCTS,
            PermissioningScope.READ_ORDERS,
        ]
        webhook_data = {
            "@context": settings.LDP_RDF_CONTEXT,
            "eventType": "grant",
            "user": self.user.urlid,
            "scopes": scopes,
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
        # Scopes created.
        self._assert_expected_scopes(scopes, user=self.user)

        # Scopes are not created for enterprises not subject to grant.
        self.assertEqual(
            AssignedScope.objects.exclude(
                proxied_obj_urlid=enterprise.proxy_of
            ).count(),
            0,
        )

        # Re-submitting the webhook does not create duplicate grants.
        response = self.client.post(
            reverse("djangoldp-dfc-webhook"),
            data=json.dumps(webhook_data),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)
        self._assert_expected_scopes(scopes, user=self.user)

        # Re-submitting with empty scopes clears the grants.
        webhook_data["scopes"] = []
        response = self.client.post(
            reverse("djangoldp-dfc-webhook"),
            data=json.dumps(webhook_data),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)
        self._assert_expected_scopes(scopes, user=self.user, count=0)
