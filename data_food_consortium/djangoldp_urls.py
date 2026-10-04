from django.urls import path
from django.views.generic.base import RedirectView

from .models import Organization, Person, SuppliedProduct
from .views import (
    CacheWebhookView,
    OrganizationImportView,
    OrganizationViewset,
    PersonViewset,
    ProxyWebIDView,
    SuppliedProductViewset,
)

urlpatterns = [
    path("profile", ProxyWebIDView.as_view()),
    path("dfc/import/", OrganizationImportView.as_view(), name="csv_import"),
    path(
        "dfc/enterprise-import/",
        RedirectView.as_view(pattern_name="csv_import"),
        name="enterprise_import",
    ),
    path(
        "djangoldp-dfc/webhook/",
        CacheWebhookView.as_view(),
        name="djangoldp-dfc-webhook",
    ),
    path(
        "organizations/",
        OrganizationViewset.urls(
            model=Organization,
            nested_fields=[
                "supplied_products",
                "social_medias",
                "catalog_items",
                "services",
                "coordinations",
                "shipping_options",
                "template_sale_sessions",
            ],
        ),
        name="organizations_view",
    ),
    path("enterprises/", RedirectView.as_view(pattern_name="organization-list")),
    path("persons/", PersonViewset.urls(model=Person)),
    path(
        "supplied_products/",
        SuppliedProductViewset.urls(model=SuppliedProduct),
    ),
]
