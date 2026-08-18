import factory

from data_food_consortium.models_common import DataServer, Platform


class AbstractPlatformFactory(factory.django.DjangoModelFactory):
    urlid = factory.Sequence(lambda n: "https://staging.myserver.com/platforms/%d" % n)

    class Meta:
        abstract = True


class DataServerFactory(AbstractPlatformFactory):
    class Meta:
        model = DataServer


class PlatformFactory(AbstractPlatformFactory):
    class Meta:
        model = Platform
