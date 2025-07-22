from django.urls import path
from .models import Enterprise, Person
from .views import EnterpriseViewset, EnterpriseImportView, PersonViewset

urlpatterns = [
    path("dfc/enterprise-import/", EnterpriseImportView.as_view(), name="csv_import"),
    path(
        "enterprises/",
        EnterpriseViewset.urls(
            model_prefix="enterprise",
            model=Enterprise,
            nested_fields=["supplied_products", "social_medias"],
        ),
    ),
    path("persons/", PersonViewset.urls(model_prefix="person", model=Person)),
]
