import random

import factory

from data_food_consortium.models import OrganizationAddress
from data_food_consortium.tests.factories.models_common import AbstractDFCFactory


def random_letter():
    return random.choice("ABCDEFGHJKLMNOPQRSTUVWXYZ")


class AbstractAddressFactory(AbstractDFCFactory):
    city = factory.Faker("word")
    country = "United Kingdom"
    postcode = factory.LazyAttribute(
        lambda _: f"{random_letter()}{random.randint(0,99):02d} {random.randint(0,9)}{random_letter()}{random_letter()}"
    )
    region = factory.Faker("word")
    street = factory.Faker("word")

    class Meta:
        abstract = True


class OrganizationAddressFactory(AbstractAddressFactory):
    address_of = factory.SubFactory(
        "data_food_consortium.tests.factories.OrganizationFactory"
    )

    class Meta:
        model = OrganizationAddress
