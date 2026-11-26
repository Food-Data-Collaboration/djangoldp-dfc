import factory

from data_food_consortium.models_permissioning import GrantPolicy, GrantRequirement


class GrantPolicyFactory(factory.django.DjangoModelFactory):
    name = factory.Faker("word")

    class Meta:
        model = GrantPolicy


class GrantRequirementFactory(factory.django.DjangoModelFactory):
    name = factory.Faker("word")
    claim_jmes_path = "name"
    policy = factory.SubFactory(GrantPolicyFactory)

    class Meta:
        model = GrantRequirement
