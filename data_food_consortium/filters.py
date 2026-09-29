from django.conf import settings
from django.db.models import Q
from rest_framework.filters import BaseFilterBackend

from data_food_consortium.auth_utils import get_required_scope_for_model
from data_food_consortium.models_permissioning import AssignedScope


class DFCGrantedPermissionsFilterBackend(BaseFilterBackend):
    def get_granted_data_servers(self, request, model):
        # Filter scopes to the scope required for this queryset (by the model),
        # and further by those granted to the user
        return (
            AssignedScope.objects.filter(scope=get_required_scope_for_model(model))
            .for_user(request.user)
            .values_list("data_server_id", flat=True)
        )

    def filter_queryset(self, request, queryset, view):
        if not settings.DFC_USER_GRANTS_ENABLED:
            return queryset
        return queryset.filter(
            Q(data_server_source=None)
            | Q(
                data_server_source__in=self.get_granted_data_servers(
                    request, queryset.model
                )
            )
        )
