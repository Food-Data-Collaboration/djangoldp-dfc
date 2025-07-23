from django.contrib import admin
from djangoldp.admin import DjangoLDPAdmin

from data_food_consortium import models


class DFCModelAdmin(DjangoLDPAdmin):
    list_display = ["urlid", "proxy_of"]


@admin.register(models.Enterprise)
class EnterpriseAdmin(DFCModelAdmin):
    pass


@admin.register(models.EnterpriseAddress)
class EnterpriseAddressAdmin(DFCModelAdmin):
    pass


@admin.register(models.SocialMedia)
class SocialMediaAdmin(DFCModelAdmin):
    pass


@admin.register(models.Person)
class PersonAdmin(DFCModelAdmin):
    pass


@admin.register(models.SuppliedProduct)
class SuppliedProductAdmin(DFCModelAdmin):
    list_display = ["urlid", "proxy_of", "name", "has_type", "supplied_by"]
