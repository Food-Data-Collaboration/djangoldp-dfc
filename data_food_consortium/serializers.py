from djangoldp.serializers import LDPSerializer
from rest_framework import fields

from data_food_consortium.models import ShippingOption


class EnterpriseSerializer(LDPSerializer):
    dropoff_points = fields.SerializerMethodField()

    def get_dropoff_points(self, obj):
        shipping_options = ShippingOption.objects.filter(
            sale_session__coordination__enterprise=obj
        )

        # NOTE: LDPSerializer cannot be used without meta args:
        #   https://git.startinblox.com/djangoldp-packages/djangoldp/-/issues/277
        meta_args = {"model": ShippingOption, "depth": 1, "fields": "__all__"}
        meta_class = type("Meta", (), meta_args)
        serializer_class = type(LDPSerializer)(
            "LDPSerializer", (LDPSerializer,), {"Meta": meta_class}
        )
        return serializer_class(shipping_options, many=True, context=self.context).data
