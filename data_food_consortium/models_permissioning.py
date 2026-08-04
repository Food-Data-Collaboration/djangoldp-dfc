from django.db import models
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
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name="assigned_scopes",
        help_text="The platform the scope is assigned to",
    )

    def __str__(self):
        return f"{self.scope} ({self.permissioned_subject})"

    @property
    def permissioned_subject(self):
        return self.platform
