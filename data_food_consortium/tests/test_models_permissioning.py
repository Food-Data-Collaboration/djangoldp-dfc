from django.db.utils import IntegrityError
from django.test import TestCase
from djangoldp.factories import UserFactory

from data_food_consortium.models_permissioning import AssignedScope
from data_food_consortium.tests.factories import DataServerFactory, PlatformFactory


class TestModelsPermissioning(TestCase):
    def test_scope_assigned_to_exactly_one_object_none_assigned(self):
        """Tests constraint assigned_to_exactly_one_object on AssignedScope model"""
        data_server = DataServerFactory()
        # No object assigned scope.
        with self.assertRaises(IntegrityError):
            AssignedScope.objects.create(data_server=data_server)

    def test_scope_assigned_to_exactly_one_object_both_assigned(self):
        # Both objects assigned scope.
        data_server = DataServerFactory()
        platform = PlatformFactory()
        user = UserFactory()
        with self.assertRaises(IntegrityError):
            AssignedScope.objects.create(
                data_server=data_server, platform=platform, user=user
            )

    def test_scope_assigned_to_exactly_one_object_either_assigned(self):
        # Either platform or user assigned scope — no exception raised.
        data_server = DataServerFactory()
        platform = PlatformFactory()
        user = UserFactory()
        AssignedScope.objects.create(data_server=data_server, platform=platform)
        AssignedScope.objects.create(data_server=data_server, user=user)
