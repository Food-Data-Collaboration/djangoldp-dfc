import factory

from data_food_consortium.models import Enterprise
from data_food_consortium.tests.factories.models_common import AbstractDFCFactory


class EnterpriseFactory(AbstractDFCFactory):
    urlid = factory.Sequence(
        lambda n: "https://staging.myserver.com/enterprises/%d" % n
    )
    enterpriseid = factory.SelfAttribute("urlid")
    email = factory.LazyAttributeSequence(
        lambda o, n: "%d@%s%d.example.com" % (n, o.name.replace(" ", "_"), n)
    )
    phone_number = factory.Sequence(lambda n: "+44%011d" % n)
    name = factory.Faker("word")
    description = factory.Faker("word")
    long_description = factory.Faker("word")
    contact_name = factory.Faker("word")
    VATnumber = factory.Sequence(lambda n: "GB%09d" % n)
    VATstatus = True

    class Meta:
        model = Enterprise
