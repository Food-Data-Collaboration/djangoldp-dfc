from django.urls import path
from .models import Enterprise, Person, SuppliedProduct
from .views import (
    CacheWebhookView,
    EnterpriseViewset,
    EnterpriseImportView,
    PersonViewset,
    SuppliedProductViewset,
)

urlpatterns = [
    path("dfc/enterprise-import/", EnterpriseImportView.as_view(), name="csv_import"),
    path(
        "djangoldp-dfc/webhook/",
        CacheWebhookView.as_view(),
        name="djangoldp-dfc-webhook",
    ),
    path(
        "enterprises/",
        EnterpriseViewset.urls(
            model=Enterprise,
            nested_fields=["supplied_products", "social_medias", "catalog_items"],
        ),
    ),
    path("persons/", PersonViewset.urls(model=Person)),
    path(
        "supplied_products/",
        SuppliedProductViewset.urls(model=SuppliedProduct),
    ),
]
