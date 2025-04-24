from djangoldp.models import Model
from djangoldp import fields


class AbstractAgent(Model):
    email = fields.EmailField(
        rdf_type="dfc-b:email", blank=True, null=True
    )  # xsd:String
    # TODO: revisit max_length parameter based on explicit or implicit limit of the ontology
    logo = fields.LDPUrlField(
        rdf_type="dfc-b:logo", max_length=255, blank=True, null=True
    )  # xsd:anyURI

    #  "dfc-b:hasSocialMedia": "http://test.host/api/dfc/enterprises/10000/social_medias/facebook",
    # one-to-many
    # hassocialmedia = models.TextField(blank=True, null=True)

    class Meta:
        abstract = True


class Enterprise(AbstractAgent):
    enterpriseid = fields.LDPUrlField(
        rdf_type="dfc-b:enterpriseID",
        blank=True,
        null=True,
        help_text="Unique Id of the Enterprise",
    )  # xsd:String
    VATnumber = fields.TextField(
        rdf_type="dfc-b:VATnumber",
        blank=True,
        null=True,
        help_text=(
            "Any Tax Registration Number that is applicable to the Enterprise, "
            "in the jurisdiction the Enterprise is operating in."
        ),
    )  # xsd:String
    VATstatus = fields.BooleanField(
        rdf_type="dfc-b:VATStatus",
        default=False,
        null=True,
        help_text="Indicates whether the Enterprise charges VAT or not",
    )  # xsd:Boolean

    class Meta:
        rdf_type = "dfc-b:Enterprise"

    def __str__(self):
        return self.urlid
