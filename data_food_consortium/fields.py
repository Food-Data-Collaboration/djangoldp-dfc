from django.contrib.contenttypes.fields import GenericForeignKey
from djangoldp.fields import LDPFieldMixin

# TODO: this should be supported in DjangoLDP, or through a contenttypes package.


class GenericForeignKey(LDPFieldMixin, GenericForeignKey):
    pass
