import factory

from data_food_consortium.enums import ProductType
from data_food_consortium.models import SuppliedProduct
from data_food_consortium.tests.factories.models_common import AbstractDFCFactory


class SuppliedProductFactory(AbstractDFCFactory):
    urlid = factory.Sequence(
        lambda n: "https://staging.myserver.com/supplied_products/%d" % n
    )
    supplied_by = factory.SubFactory("tests.factories.OrganizationFactory")
    name = factory.Faker("word")
    description = factory.Faker("word")
    has_type = factory.Faker("random_element", elements=ProductType.values)

    class Meta:
        model = SuppliedProduct
