from django.conf import settings
from django.contrib import admin
from djangoldp.admin import DjangoLDPAdmin

from data_food_consortium import models
from data_food_consortium.enums import ResourceImportSource
from data_food_consortium.proxy.resource import ProxyRefreshParser


class DFCModelAdmin(DjangoLDPAdmin):
    list_display = ["urlid", "proxy_of", "data_server_source", "updated_at"]
    search_fields = ["urlid", "proxy_of"]
    readonly_fields = ["created_at", "updated_at"]


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
    list_display = [
        "urlid",
        "proxy_of",
        "data_server_source",
        "name",
        "has_type",
        "supplied_by",
    ]


@admin.register(models.CatalogItem)
class CatalogItemAdmin(DFCModelAdmin):
    search_fields = [
        "urlid",
        "proxy_of",
        "managed_by__name",
        "managed_by__urlid",
        "managed_by__proxy_of",
        "references__name",
        "references__urlid",
        "references__proxy_of",
    ]
    list_display = [
        "urlid",
        "proxy_of",
        "data_server_source",
        "managed_by",
        "references",
    ]
    raw_id_display = ["managed_by", "references"]


@admin.register(models.PhysicalPlace)
class PhysicalPlaceAdmin(DFCModelAdmin):
    search_fields = [
        "urlid",
        "proxy_of",
        "address__city",
        "address__country",
        "address__postcode",
        "address__region",
        "address__street",
        "main_contact__urlid",
        "main_contact__proxy_of",
        "main_contact__first_name",
        "main_contact__last_name",
        "main_contact__email",
        "URL",
        "phone_number",
    ]
    raw_id_fields = ["main_contact"]


@admin.register(models.Coordination)
class CoordinationAdmin(DFCModelAdmin):
    search_fields = [
        "urlid",
        "proxy_of",
        "name",
        "enterprise__name",
        "enterprise__urlid",
        "enterprise__proxy_of",
    ]
    list_display = ["urlid", "name", "enterprise"]
    raw_id_fields = ["enterprise"]


@admin.register(models.SaleSession)
class SaleSessionAdmin(DFCModelAdmin):
    list_display = ["urlid", "coordination", "start_date", "end_date"]
    raw_id_fields = ["hosted_at", "coordination"]


@admin.register(models.ShippingOption)
class ShippingOptionAdmin(DFCModelAdmin):
    list_display = ["urlid", "sale_session", "has_type"]
    list_filter = ["has_type"]
    raw_id_fields = ["sale_session", "picked_up_at", "delivers_at"]


@admin.action(description="Retry import")
def retry_import(modeladmin, request, queryset):
    for record in queryset:
        for data_batch in record.data_batches:
            parser = ProxyRefreshParser(record.data_server_source)
            parser.parse(data_batch)
            parser.clean_up()
            if settings.DFC_STORE_IMPORT_REPORTS:
                parser.create_record(ResourceImportSource.ADMIN_SITE)


@admin.register(models.ResourceImportRecord)
class ResourceImportRecordAdmin(admin.ModelAdmin):
    list_display = ["import_started_at", "data_server_source", "source"]
    list_filter = ["source"]
    readonly_fields = ["parsed_data"]
    actions = [retry_import]
