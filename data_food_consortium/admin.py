from django.contrib import admin
from djangoldp.admin import DjangoLDPAdmin

from data_food_consortium import models


class DFCModelAdmin(DjangoLDPAdmin):
    list_display = ["urlid", "proxy_of"]
    search_fields = ["urlid", "proxy_of"]


@admin.register(models.Enterprise)
class EnterpriseAdmin(DFCModelAdmin):
    search_fields = ["urlid", "proxy_of", "name"]


@admin.register(models.EnterpriseAddress)
class EnterpriseAddressAdmin(DFCModelAdmin):
    search_fields = [
        "urlid",
        "proxy_of",
        "city",
        "country",
        "postcode",
        "region",
        "street",
        "address_of__urlid",
        "address_of__name",
        "address_of__proxy_of",
    ]


@admin.register(models.SocialMedia)
class SocialMediaAdmin(DFCModelAdmin):
    search_fields = [
        "urlid",
        "proxy_of",
        "url",
        "enterprise__urlid",
        "enterprise__name",
        "enterprise__proxy_of",
    ]


@admin.register(models.Person)
class PersonAdmin(DFCModelAdmin):
    search_fields = [
        "first_name",
        "last_name",
        "proxy_of",
        "urlid",
        "email",
        "phone_number",
    ]


@admin.register(models.Service)
class ServiceAdmin(DFCModelAdmin):
    search_fields = ["urlid", "proxy_of", "name"]
    list_display = ["name"]


@admin.register(models.EnterpriseService)
class EnterpriseServiceAdmin(DFCModelAdmin):
    search_fields = [
        "urlid",
        "proxy_of",
        "service__name",
        "service__urlid",
        "enterprise__name",
        "enterprise__urlid",
        "enterprise__proxy_of",
    ]
    list_display = ["enterprise", "service"]
    raw_id_fields = ["enterprise"]


@admin.register(models.SuppliedProduct)
class SuppliedProductAdmin(DFCModelAdmin):
    search_fields = [
        "urlid",
        "proxy_of",
        "name",
        "has_type",
        "supplied_by__name",
        "supplied_by__urlid",
        "supplied_by__proxy_of",
    ]
    list_display = ["urlid", "proxy_of", "name", "has_type", "supplied_by"]
