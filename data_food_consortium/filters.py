from django.conf import settings
from django.db.models import Q
from rest_framework.filters import BaseFilterBackend

from data_food_consortium.auth_utils import get_required_scope_for_model
from data_food_consortium.models_permissioning import AssignedScope


class DFCGrantedPermissionsFilterBackend(BaseFilterBackend):
    def get_assigned_scopes_for_user(self, request, model):
        return AssignedScope.objects.filter(
            scope=get_required_scope_for_model(model)
        ).for_user(request.user)

    def filter_queryset(self, request, queryset, view):
        if not settings.DFC_USER_GRANTS_ENABLED:
            return queryset

        assigned_scopes = self.get_assigned_scopes_for_user(request, queryset.model)
        objects_by_general_grant = Q(
            data_server_source_id__in=assigned_scopes.filter(
                proxied_obj_urlid="all"
            ).values_list("data_server_id", flat=True)
        )
        objects_by_specific_grant = Q(
            proxy_of__in=assigned_scopes.values_list("proxied_obj_urlid", flat=True)
        )

        return queryset.filter(
            Q(data_server_source=None)
            | objects_by_general_grant
            | objects_by_specific_grant
        )
