from django.test import TestCase, override_settings
from djangoldp.models import Model
from rest_framework.test import APIClient

from data_food_consortium.auth_utils import user_oidc_provider
from data_food_consortium.enums import PermissioningScope
from data_food_consortium.models import Organization
from data_food_consortium.models_permissioning import AssignedScope
from data_food_consortium.tests.factories import (
    DFCUserFactory,
    OrganizationFactory,
    PlatformFactory,
    SuppliedProductFactory,
)


class TestFiltersPermissioning(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = DFCUserFactory(is_superuser=False)
        self.user_platform = PlatformFactory(urlid=user_oidc_provider(self.user))
        self.client.force_authenticate(self.user)

    def _test_direct_resource_access(self, resource, can_access):
        response = self.client.get(
            Model.resource(resource), content_type="application/ld+json"
        )
        if can_access:
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.data["@id"], resource.urlid)
        else:
            self.assertEqual(response.status_code, 404)
        return response

    def test_filter_disabled_by_setting(self):
        """
        By default, DFC_USER_GRANTS_ENABLED is False. This test ensures that it correctly disables
        filtering by granted permissions.
        """
        org = (
            OrganizationFactory()
        )  # I have not been granted specific permissions to access.

        response = self.client.get(
            Model.resource(Organization), content_type="application/ld+json"
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data["ldp:contains"]), 1)
        assert response.data["ldp:contains"][0]["@id"] == org.urlid

        # GET the test organizations directly.
        self._test_direct_resource_access(org, True)

    @override_settings(DFC_USER_GRANTS_ENABLED=True)
    def test_filter_granted_organizations(self):
        # Set up two organizations which I have permission to access, by a general grant.
        org_general_grant = OrganizationFactory()
        SuppliedProductFactory(
            supplied_by=org_general_grant,
            data_server_source=org_general_grant.data_server_source,
            name="Organisation by general grant",
        )
        AssignedScope.objects.create(
            data_server=org_general_grant.data_server_source,
            scope=PermissioningScope.READ_ENTERPRISE,
            user=self.user,
            proxied_obj_urlid="all",
        )

        # Set up an organizations which I do have permission to access, by specific grant.
        org_granted_to_me = OrganizationFactory()
        SuppliedProductFactory(
            supplied_by=org_granted_to_me,
            data_server_source=org_granted_to_me.data_server_source,
            name="Organisation by specific grant",
        )
        AssignedScope.objects.create(
            data_server=org_granted_to_me.data_server_source,
            scope=PermissioningScope.READ_ENTERPRISE,
            user=self.user,
            proxied_obj_urlid=org_granted_to_me.proxy_of,
        )

        # Set up an organization which I have permission to access, by my platform.
        org_granted_to_my_platform = OrganizationFactory()
        SuppliedProductFactory(
            supplied_by=org_granted_to_my_platform,
            data_server_source=org_granted_to_my_platform.data_server_source,
            name="Organisation by platform grant",
        )
        AssignedScope.objects.create(
            data_server=org_granted_to_my_platform.data_server_source,
            scope=PermissioningScope.READ_ENTERPRISE,
            platform=self.user_platform,
            proxied_obj_urlid=org_granted_to_my_platform.proxy_of,
        )

        # Set up an organization which I have the wrong scope to access.
        only_products_org = OrganizationFactory()
        granted_product = SuppliedProductFactory(
            supplied_by=only_products_org,
            data_server_source=only_products_org.data_server_source,
            name="Granted product",
        )
        AssignedScope.objects.create(
            data_server=only_products_org.data_server_source,
            scope=PermissioningScope.READ_PRODUCTS,
            user=self.user,
            proxied_obj_urlid=granted_product.proxy_of,
        )

        # Set up an organization which I cannot access, from a known data server.
        non_granted_org = OrganizationFactory(
            data_server_source=org_granted_to_my_platform.data_server_source
        )
        SuppliedProductFactory(
            supplied_by=non_granted_org,
            data_server_source=org_granted_to_my_platform.data_server_source,
            name="Non granted organisation",
        )
        # and from an unacquianted data server.
        unknown_org = OrganizationFactory()
        SuppliedProductFactory(
            supplied_by=unknown_org,
            data_server_source=unknown_org.data_server_source,
            name="Product from third organisation",
        )

        # GET organizations, test that the filters are applied.
        response = self.client.get(
            Model.resource(Organization), content_type="application/ld+json"
        )
        self.assertEqual(response.status_code, 200)
        # Assert view has filtered out those without permission.
        self.assertEqual(len(response.data["ldp:contains"]), 3)
        serialized_urlids = {o["@id"] for o in response.data["ldp:contains"]}
        self.assertEqual(
            len(
                serialized_urlids.difference(
                    {
                        org_general_grant.urlid,
                        org_granted_to_me.urlid,
                        org_granted_to_my_platform.urlid,
                    }
                )
            ),
            0,
        )

        # GET the test organizations directly.
        self._test_direct_resource_access(org_general_grant, True)
        self._test_direct_resource_access(org_granted_to_me, True)
        self._test_direct_resource_access(org_granted_to_my_platform, True)
        self._test_direct_resource_access(only_products_org, False)
        self._test_direct_resource_access(non_granted_org, False)
        self._test_direct_resource_access(unknown_org, False)

        # permissions on nested containers - products have not been granted.
        for serialized_org in response.data["ldp:contains"]:
            self.assertEqual(len(serialized_org["dfc-b:supplies"]["ldp:contains"]), 0)

        # only the following organisation has granted both read enterprise and products.
        AssignedScope.objects.create(
            data_server=only_products_org.data_server_source,
            scope=PermissioningScope.READ_ENTERPRISE,
            user=self.user,
            proxied_obj_urlid=only_products_org.proxy_of,
        )
        response = self._test_direct_resource_access(only_products_org, True)
        supplied_product_serialization = response.data["dfc-b:supplies"]["ldp:contains"]
        self.assertEqual(len(supplied_product_serialization), 1)
        self.assertEqual(
            supplied_product_serialization[0]["@id"], granted_product.urlid
        )
