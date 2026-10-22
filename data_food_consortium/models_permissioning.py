import jmespath
from django.conf import settings
from django.db import models
from django.db.models import Q
from djangoldp import fields
from djangoldp.models import LDPModelManager, Model

from data_food_consortium.auth_utils import (
    get_required_scope_for_model,
    user_oidc_provider,
)
from data_food_consortium.enums import PermissioningScope
from data_food_consortium.models_common import DataServer, Platform
from data_food_consortium.utils import whitespace_dict


class AssignedScopeQuerySet(models.QuerySet):
    def for_model_scope(self, model):
        return self.filter(scope=get_required_scope_for_model(model))

    def for_user(self, user):
        # Filter by those given to the user as an individual and by virtue of the user's platform.
        platform = Platform.objects.get_or_create(urlid=user_oidc_provider(user))[0]
        return self.filter(Q(platform=platform) | Q(user=user))

    def for_obj(self, obj):
        """
        Scopes granted to a specific object, directly or indirectly.
        """
        return self.filter(
            Q(proxied_obj_urlid=obj.proxy_of)
            | Q(Q(proxied_obj_urlid="all") & Q(data_server=obj.data_server_source))
        )


class AssignedScopeModelManager(LDPModelManager):
    def get_queryset(self):
        return AssignedScopeQuerySet(self.model, using=self._db)

    def for_model_scope(self, model):
        return self.get_queryset().for_model_scope(model)

    def for_user(self, user):
        return self.get_queryset().for_user()


class AssignedScope(Model):
    data_server = fields.ForeignKey(
        DataServer,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name="granted_scopes",
        help_text="The organization (producer) which granted and controls the scope",
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
    proxied_obj_urlid = fields.TextField(
        help_text="The urlid of the object upon which the scope is granted. Set to 'all', the user can access all objects"
    )
    objects = AssignedScopeModelManager()

    class Meta(Model.Meta):
        constraints = [
            models.CheckConstraint(
                check=(Q(platform__isnull=False) & Q(user__isnull=True))
                | (Q(platform__isnull=True) & Q(user__isnull=False)),
                name="assigned_to_exactly_one_subject",
            ),
            models.CheckConstraint(
                check=~(Q(proxied_obj_urlid__isnull=True) | Q(proxied_obj_urlid="")),
                name="assigned_to_object",
            ),
        ]

    def __str__(self):
        return f"{self.scope} ({self.permissioned_object})"

    @property
    def permissioned_object(self):
        return self.platform if self.platform is not None else self.user


class GrantRequirement(Model):
    """
    Custom restriction made on user claims for access to a resource.
    """

    name = models.CharField(
        max_length=32, help_text="A short unique identifier with no spaces", unique=True
    )
    claim_jmes_path = models.TextField(
        help_text="JMESPath expression on the standard user claims"
    )
    requires_false = models.BooleanField(
        default=False,
        help_text="The condition described by this requirement must not be met (applies a NOT in boolean logic).",
    )
    policy = models.ForeignKey(
        "GrantPolicy",
        verbose_name="Grant policy",
        on_delete=models.CASCADE,
        related_name="requirements",
    )

    class Meta(Model.Meta):
        pass

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.translate(whitespace_dict)
        if self.id is None and GrantRequirement.objects.filter(name=self.name).exists():
            self.name = f"{self.name}_{self.id}"
        super().save(*args, **kwargs)

    def compile_jmes(self):
        return jmespath.compile(self.claim_jmes_path)

    def test(self, user_claims):
        compiled_jmes = self.compile_jmes()
        return compiled_jmes.search(user_claims) != None


class GrantPolicy(Model):
    """
    A policy is a collection of requirements.
    They are made on a resource, or category of resources, by a model which leverages the policy.
    """

    name = models.CharField(
        max_length=32, help_text="A short unique identifier with no spaces", unique=True
    )
    requires_false = models.BooleanField(
        default=False,
        help_text="The condition described by this policy must not be met (applies a NOT in boolean logic).",
    )

    class Meta(Model.Meta):
        pass

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.translate(whitespace_dict)
        super().save(*args, **kwargs)

    def test(self, user_claims):
        # If a single requirement fails, the test fails. Expressions allowing OR/brackets etc are TODO.
        for requirement in self.requirements.all():
            if not requirement.test(user_claims):
                return False
        return True


class DataServerGrantPolicy(Model):
    """
    Implements a grant policy by associating it to a DataServer.
    """

    data_server = models.ForeignKey(
        DataServer, on_delete=models.CASCADE, related_name="policies"
    )
    policy = models.ForeignKey(
        GrantPolicy,
        verbose_name="Grant policy",
        on_delete=models.CASCADE,
        related_name="data_servers",
    )

    class Meta(Model.Meta):
        pass

    def __str__(self):
        return f"{self.data_server} policy {self.policy}"
