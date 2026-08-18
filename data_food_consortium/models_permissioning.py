from django.conf import settings
from django.db import models
from django.db.models import Q
from djangoldp import fields
from djangoldp.models import Model

from data_food_consortium.enums import PermissioningScope
from data_food_consortium.models_common import DataServer, Platform


class AssignedScope(Model):
    data_server = fields.ForeignKey(
        DataServer,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name="granted_scopes",
        help_text="The enterprise (producer) which granted and controls the scope",
    )
    scope = fields.CharField(
        # rdf_type="dfc-b:hasType",  # TODO: what is the RDF type?
        help_text="The scope assigned, a permission granted (absence of scope implicitly means absence of permission)",
        choices=PermissioningScope.choices,
        blank=True,
        null=True,
        default=PermissioningScope.READ_PRODUCTS,
        max_length=255,
    )
    platform = fields.ForeignKey(
        Platform,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="assigned_scopes",
        help_text="A scope can be assigned to a platform, and all of its members",
    )
    user = fields.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="assigned_scopes",
        help_text="A scope can be assigned to an individual user",
    )

    class Meta(Model.Meta):
        constraints = [
            models.CheckConstraint(
                check=(Q(platform__isnull=False) & Q(user__isnull=True))
                | (Q(platform__isnull=True) & Q(user__isnull=False)),
                name="assigned_to_exactly_one_object",
            ),
        ]

    def __str__(self):
        return f"{self.scope} ({self.permissioned_object})"

    @property
    def permissioned_object(self):
        return self.platform if self.platform is not None else self.user
