from django.template.defaultfilters import striptags
from djangoldp_open_world_model.serializers import OpenWorldLDPSerializer
from rest_framework import fields, serializers


class StrippedHTMLCharField(fields.CharField):
    def to_internal_value(self, data):
        return striptags(super().to_internal_value(data))


class LDPSerializerDFC(OpenWorldLDPSerializer):
    pass


class OrganizationSerializer(LDPSerializerDFC):
    description = StrippedHTMLCharField(
        allow_blank=True, allow_null=True, required=False
    )
    long_description = StrippedHTMLCharField(
        allow_blank=True, allow_null=True, required=False
    )


class ProductSerializer(LDPSerializerDFC):
    description = StrippedHTMLCharField(
        allow_blank=True, allow_null=True, required=False
    )
    has_type = serializers.CharField(
        required=False
    )  # Not required to be a known ProductType.
