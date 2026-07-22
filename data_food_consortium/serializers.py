from django.template.defaultfilters import striptags
from rest_framework import serializers

from djangoldp.serializers import LDPSerializer
from rest_framework import fields


class StrippedHTMLCharField(fields.CharField):
    def to_internal_value(self, data):
        return striptags(super().to_internal_value(data))


class EnterpriseSerializer(LDPSerializer):
    description = StrippedHTMLCharField(
        allow_blank=True, allow_null=True, required=False
    )
    long_description = StrippedHTMLCharField(
        allow_blank=True, allow_null=True, required=False
    )


class ProductSerializer(LDPSerializer):
    description = StrippedHTMLCharField(
        allow_blank=True, allow_null=True, required=False
    )
    has_type = serializers.CharField(
        required=False
    )  # Not required to be a known ProductType.
