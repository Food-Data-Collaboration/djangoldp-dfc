from django.conf import settings
from djangoldp.permissions import LDPBasePermission

from data_food_consortium.filters import DFCGrantedPermissionsFilterBackend
from data_food_consortium.models_permissioning import AssignedScope


class DFCPermission(LDPBasePermission):
    filter_backend = DFCGrantedPermissionsFilterBackend

    def get_assigned_scopes_for_obj(self, request, model, obj):
        return (
            AssignedScope.objects.for_model_scope(model)
            .for_user(request.user)
            .for_obj(obj)
        )

    def user_has_tag_for_object_from_data_server(self, request, obj):
        user_tags = request.user.dfc_tags.filter(
            data_server=obj.data_server_source
        ).first()
        if user_tags is None:
            return False

        user_tags = set(user_tags.tags.all())
        return len(user_tags.intersection(set(obj.perms_tags.all()))) > 0

    def user_passes_all_data_server_policies(self, request, obj):
        for dsp in obj.data_server_source.policies.all():
            if not dsp.policy.test(request.user_claims):
                return False
        return True

    def has_object_permission(self, request, view, obj):
        if not settings.DFC_USER_GRANTS_ENABLED or request.user.is_superuser:
            return True
        has_valid_grant = (
            self.get_assigned_scopes_for_obj(request, type(obj), obj).count() > 0
        )
        return (
            has_valid_grant
            or self.user_has_tag_for_object_from_data_server(request, obj)
            or self.user_passes_all_data_server_policies(request, obj)
        ) and super().has_object_permission(request, view, obj)
