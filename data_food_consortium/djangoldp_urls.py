from django.urls import path
from .models import Enterprise
from .views import EnterpriseViewset

urlpatterns = [
    path(
        "enterpsies/",
        EnterpriseViewset.urls(model_prefix="enterprise", model=Enterprise),
    )
]
