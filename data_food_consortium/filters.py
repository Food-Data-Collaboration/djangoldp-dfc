from django.conf import settings
from django.db.models import Count, Q
from rest_framework.filters import BaseFilterBackend

from data_food_consortium.models_common import DataServer
from data_food_consortium.models_permissioning import AssignedScope


class DFCGrantedPermissionsFilterBackend(BaseFilterBackend):
    def get_assigned_scopes_for_user(self, request, model):
        return AssignedScope.objects.for_model_scope(model).for_user(request.user)

    def filter_queryset(self, request, queryset, view):
        if not settings.DFC_USER_GRANTS_ENABLED:
            return queryset

        # Scopes assigned to me by Data Server policy.
        # This means that my user claims pass the tests set by the Data Server.
        # TODO: currently these are data-server wide and not by-object.
        data_servers = (
            DataServer.objects.filter(
                id__in=queryset.values_list(
                    "data_server_source_id", flat=True
                ).distinct()
            )
            .annotate(policy_count=Count("policies"))
            .filter(policy_count__gt=0)
        )
        data_server_ids = []
        for d in data_servers:
            passes_test = True
            for dsp in d.policies.all():
                if not dsp.policy.test(request.user_claims):
                    passes_test = False
                    break
            if passes_test:
                data_server_ids.append(d.id)

        # Scopes assigned to me or my platform, by object or data server.
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
            | Q(data_server_source_id__in=data_server_ids)
            | objects_by_general_grant
            | objects_by_specific_grant
        )
