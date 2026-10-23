import uuid

from django.db.utils import IntegrityError
from django.test import TestCase

from data_food_consortium.models_permissioning import AssignedScope
from data_food_consortium.tests.factories import (
    DataServerFactory,
    DFCUserFactory,
    GrantRequirementFactory,
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


class TestGrantRequirements(TestCase):
    def _get_example_user_claims(self, user=None):
        if user is None:
            user = DFCUserFactory()

        return {
            "sub": str(uuid.uuid4()),
            "webid": user.urlid,
            "email_verified": True,
            "name": f"{user.first_name} {user.last_name}",
            "preferred_username": user.username,
            "given_name": user.first_name,
            "family_name": user.last_name,
            "email": user.email,
        }

    def test_jmes_path_resolution(self):
        user_claims = self._get_example_user_claims()
        # Add an extra field with a complex structure.
        user_claims["characters"] = [{"name": "The Grudge"}, {"name": "Smiley"}]
        full_name = user_claims["name"]
        jmes_examples = {
            "name": full_name,
            f"name=='{full_name}'": True,
            "characters[?name=='Smiley'].name | [0]": "Smiley",
            "characters[?name=='Mystery Man'].name | [0]": None,
        }
        gr = GrantRequirementFactory()
        for path, expected_result in jmes_examples.items():
            gr.claim_jmes_path = path
            gr.save()
            compiled_jmes = gr.compile_jmes()
            self.assertEqual(compiled_jmes.search(user_claims), expected_result)

    def test_grant_requirements_resolution(self):
        user_claims = self._get_example_user_claims()
        gr = GrantRequirementFactory(
            claim_jmes_path="groups[?name=='The Inner Circle'] | [0]"
        )
        policy = gr.policy
        self.assertFalse(gr.test(user_claims))
        self.assertFalse(policy.test(user_claims))

        user_claims["groups"] = [{"name": "The Inner Circle"}]
        self.assertTrue(gr.test(user_claims))
        self.assertTrue(policy.test(user_claims))

        # Add a second GrantRequirement to policy, which is not true.
        gr_b = GrantRequirementFactory(
            claim_jmes_path="groups[?name=='The Outer Square'] | [0]",
            policy=policy,
        )
        self.assertTrue(gr.test(user_claims))
        self.assertFalse(gr_b.test(user_claims))
        self.assertFalse(policy.test(user_claims))

        # When the second requirement passes as well, so does the policy.
        user_claims["groups"].append({"name": "The Outer Square"})
        self.assertTrue(gr.test(user_claims))
        self.assertTrue(gr_b.test(user_claims))
        self.assertTrue(policy.test(user_claims))
