from django.db import models
from djangoldp.models import Model
from djangoldp import fields


class AbstractAddress(Model):
    city = fields.TextField(rdf_type="dfc-b:hasCity", blank=True, null=True)
    country = fields.TextField(rdf_type="dfc-b:hasCountry", blank=True, null=True)
    latitude = fields.TextField(rdf_type="dfc-b:latitude", blank=True, null=True)
    longitude = fields.TextField(rdf_type="dfc-b:longitude", blank=True, null=True)
    postcode = fields.TextField(rdf_type="dfc-b:hasPostalCode", blank=True, null=True)
    region = fields.TextField(rdf_type="dfc-b:region", blank=True, null=True)
    street = fields.TextField(rdf_type="dfc-b:hasStreet", blank=True, null=True)

    class Meta(Model.Meta):
        abstract = True
        rdf_type = "dfc-b:Address"


class AbstractAgent(Model):
    email = fields.EmailField(
        rdf_type="dfc-b:email", blank=True, null=True
    )  # xsd:String
    # TODO: revisit max_length parameter based on explicit or implicit limit of the ontology
    logo = fields.LDPUrlField(
        rdf_type="dfc-b:logo", max_length=255, blank=True, null=True
    )  # xsd:anyURI
    logo_url = fields.LDPUrlField(
        rdf_type="ofn:logo_url", max_length=255, blank=True, null=True
    )
    promo_image_url = fields.LDPUrlField(
        rdf_type="ofn:promo_image_url", max_length=255, blank=True, null=True
    )
    phone_number = fields.TextField(
        rdf_type="dfc-b:hasPhoneNumber", blank=True, null=True
    )

    class Meta(Model.Meta):
        abstract = True


class Enterprise(AbstractAgent):
    enterpriseid = fields.LDPUrlField(
        rdf_type="dfc-b:enterpriseID",
        blank=True,
        null=True,
        help_text="Unique Id of the Enterprise",
    )  # xsd:String
    name = fields.TextField(rdf_type="dfc-b:name", blank=True, null=True)  # xsd:String
    description = fields.TextField(
        rdf_type="dfc-b:hasDescription", blank=True, null=True
    )
    long_description = fields.TextField(
        rdf_type="ofn:long_description", blank=True, null=True
    )
    contact_name = fields.TextField(
        rdf_type="ofn:contact_name",
        blank=True,
        null=True,
        help_text="Name of the primary contact (from the OFN ontology)",
    )
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

    class Meta(AbstractAgent.Meta):
        rdf_type = "dfc-b:Enterprise"
        depth = 1
        nested_fields = ["addresses", "social_medias", "affiliates"]

    def __str__(self):
        return self.urlid

    # coordinates = models.TextField(blank=True, null=True) # Reverse on Coordination model
    # defines = models.TextField(blank=True, null=True) # Reverse on CustomerCategory model
    # maintains = models.TextField(blank=True, null=True) reverse on Catalog
    # manages = models.TextField(blank=True, null=True) reverse on CatalogItem
    # orders = models.TextField(blank=True, null=True) from subclassing Agent. Reverse on Orders
    # owns = models.TextField(blank=True, null=True) from subclassing Agent. Reverse on Brand
    # proposes = models.TextField(blank=True, null=True) reverse on TechnicalProduct
    # requests = models.TextField(blank=True, null=True) reverse on FunctionalProduct
    # sells = models.TextField(blank=True, null=True) FK to model Order
    # The entity responsible for the sale (could be the Enterprise or a Salesperson within that Enterprise, or a third party)
    # supplies = models.TextField(blank=True, null=True) reverse on SuppliedProduct
    # transforms = models.TextField(blank=True, null=True) FK to model "as planned local transformation"


class EnterpriseAddress(AbstractAddress):
    # TODO: should be rendered as hasAddresses
    address_of = fields.ForeignKey(
        Enterprise,
        rdf_type="dfc-b:addressOf",
        related_name="addresses",
        on_delete=models.CASCADE,
    )

    class Meta(AbstractAddress.Meta):
        pass

    def __str__(self):
        return f"{self.address_of} address"


class SocialMedia(Model):
    enterprise = fields.ForeignKey(
        Enterprise,
        rdf_type="dfc-b:hasSocialMedia",
        related_name="social_medias",
        on_delete=models.CASCADE,
    )
    name = fields.TextField(rdf_type="dfc-b:name", blank=True, null=True)  # xsd:String
    url = fields.LDPUrlField(rdf_type="dfc-b:URL", blank=True, null=True)

    class Meta(Model.Meta):
        rdf_type = "dfc-b:SocialMedia"

    def __str__(self):
        return f"{self.enterprise}: {self.name}"


class Person(AbstractAgent):
    # TODO: a Person is affiliated to an Enterprise via an EnterpriseGroup, not directly?
    # this contradicts the ontology
    affiliated_to = fields.ForeignKey(
        Enterprise,
        rdf_type="dfc-b:affiliatedTo",
        blank=True,
        null=True,
        related_name="affiliates",
        on_delete=models.SET_NULL,
    )
    first_name = fields.TextField(rdf_type="dfc-b:firstName", blank=True, null=True)
    last_name = fields.TextField(rdf_type="dfc-b:familyName", blank=True, null=True)
    # TODO: a person can be the dfc-b:mainContactOf an Enterprise or a PhysicalPlace.
    # This will need to be a generic foreign key (ManyToMany)

    class Meta:
        rdf_type = "dfc-b:Person"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
