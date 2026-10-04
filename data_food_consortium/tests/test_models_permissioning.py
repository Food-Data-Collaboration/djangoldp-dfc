from django.db.utils import IntegrityError
from django.test import TestCase

from data_food_consortium.models_permissioning import AssignedScope
from data_food_consortium.tests.factories import (
    DataServerFactory,
    DFCUserFactory,
    PlatformFactory,
)


class TestModelsPermissioning(TestCase):
    def test_assigned_scope_constraint_exactly_one_subject(self):
        data_server = DataServerFactory()
        # No subject assigned scope.
        with self.assertRaises(IntegrityError):
            AssignedScope.objects.create(
                data_server=data_server, proxied_obj_urlid="all"
            )

    def test_assigned_scope_constraint_exactly_one_object(self):
        data_server = DataServerFactory()
        # No object assigned scope.
        with self.assertRaises(IntegrityError):
            AssignedScope.objects.create(
                data_server=data_server, platform=PlatformFactory()
            )

    def test_scope_assigned_to_exactly_one_object_both_assigned(self):
        # Both objects assigned scope.
        data_server = DataServerFactory()
        platform = PlatformFactory()
        user = DFCUserFactory()
        with self.assertRaises(IntegrityError):
            AssignedScope.objects.create(
                data_server=data_server, platform=platform, user=user
            )

    def test_scope_assigned_to_exactly_one_object_either_assigned(self):
        # Either platform or user assigned scope — no exception raised.
        data_server = DataServerFactory()
        platform = PlatformFactory()
        user = DFCUserFactory()
        AssignedScope.objects.create(
            data_server=data_server, platform=platform, proxied_obj_urlid="all"
        )
        AssignedScope.objects.create(
            data_server=data_server, user=user, proxied_obj_urlid="all"
        )
