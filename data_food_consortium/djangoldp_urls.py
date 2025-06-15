from django.urls import path
from .models import Enterprise
from .views import EnterpriseViewset

urlpatterns = [
    path(
        "enterprises/",
        EnterpriseViewset.urls(
            model_prefix="enterprise",
            model=Enterprise,
            nested_fields=["supplied_products"],
        ),
    )
]
