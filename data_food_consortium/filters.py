from django.conf import settings
from django.db.models import Count, OuterRef, Q, Subquery
from django.db.models.fields import IntegerField
from rest_framework.filters import BaseFilterBackend

from data_food_consortium.models_permissioning import AssignedScope, UserTagGrant


class DFCGrantedPermissionsFilterBackend(BaseFilterBackend):
    def get_assigned_scopes_for_user(self, request, model):
        return AssignedScope.objects.for_model_scope(model).for_user(request.user)

    def filter_queryset(self, request, queryset, view):
        if not settings.DFC_USER_GRANTS_ENABLED:
            return queryset

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

        # Scopes assigned to me by tag.
        # Objects with a tag from a grant I have, data Server also matches
        queryset = queryset.annotate(
            matching_tags=Subquery(
                UserTagGrant.objects.filter(
                    user=request.user,
                    data_server=OuterRef("data_server_source"),
                    tags__in=OuterRef("perms_tags"),
                )
                .annotate(cnt=Count("id"))
                .values("cnt"),
                output_field=IntegerField(),
            )
        )

        return queryset.filter(
            Q(data_server_source=None)
            | objects_by_general_grant
            | objects_by_specific_grant
            | Q(matching_tags__gt=0)
        )
