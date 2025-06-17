from django.db import models
from djangoldp.models import Model
from djangoldp import fields

from data_food_consortium.enums import ProductType


class AbstractDFCModel(Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    data_server_source = fields.TextField(
        help_text="The URL of the dataserver which provided the instance"
    )

    class Meta(Model.Meta):
        abstract = True
        serializer_fields = ["@id", "data_server_source"]


class AbstractAddress(AbstractDFCModel):
    city = fields.TextField(
        rdf_type="dfc-b:hasCity",
        blank=True,
        null=True,
    )
    country = fields.TextField(
        rdf_type="dfc-b:hasCountry",
        blank=True,
        null=True,
    )
    latitude = fields.TextField(
        rdf_type="dfc-b:latitude",
        blank=True,
        null=True,
    )
    longitude = fields.TextField(
        rdf_type="dfc-b:longitude",
        blank=True,
        null=True,
    )
    postcode = fields.TextField(
        rdf_type="dfc-b:hasPostalCode",
        blank=True,
        null=True,
    )
    region = fields.TextField(
        rdf_type="dfc-b:region",
        blank=True,
        null=True,
    )
    street = fields.TextField(
        rdf_type="dfc-b:hasStreet",
        blank=True,
        null=True,
    )

    class Meta(AbstractDFCModel.Meta):
        abstract = True


class AbstractAgent(AbstractDFCModel):
    email = fields.EmailField(
        rdf_type="dfc-b:email",
        blank=True,
        null=True,
    )  # xsd:String
    # TODO: revisit max_length parameter based on explicit or implicit limit of the ontology
    logo = fields.LDPUrlField(
        rdf_type="dfc-b:logo",
        max_length=255,
        blank=True,
        null=True,
    )  # xsd:anyURI
    logo_url = fields.LDPUrlField(
        rdf_type="ofn:logo_url", max_length=255, blank=True, null=True
    )
    promo_image_url = fields.LDPUrlField(
        rdf_type="ofn:promo_image_url", max_length=255, blank=True, null=True
    )
    phone_number = fields.TextField(
        rdf_type="dfc-b:hasPhoneNumber",
        blank=True,
        null=True,
    )

    class Meta(AbstractDFCModel.Meta):
        abstract = True


class Enterprise(AbstractAgent):
    enterpriseid = fields.LDPUrlField(
        rdf_type="dfc-b:enterpriseID",
        blank=True,
        null=True,
        help_text="Unique Id of the Enterprise",
    )  # xsd:String
    name = fields.TextField(
        rdf_type="dfc-b:name",
        blank=True,
        null=True,
    )  # xsd:String
    description = fields.TextField(
        rdf_type="dfc-b:hasDescription",
        blank=True,
        null=True,
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
        serializer_fields = [
            "@id",
            "name",
            "email",
            "logo",
            "logo_url",
            "promo_image_url",
            "phone_number",
            "description",
            "long_description",
            "contact_name",
            "VATnumber",
            "VATstatus",
            "addresses",
            "social_medias",
            "affiliates",
            "data_server_source",
        ]
        nested_fields = ["addresses", "social_medias", "affiliates"]
        disable_url = True  # Disables DjangoLDP auto-url generation

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
    address_of = fields.ForeignKey(
        Enterprise,
        related_rdf_type="dfc-b:hasAddress",
        rdf_type="dfc-b:addressOf",
        blank=True,
        null=True,
        related_name="addresses",
        on_delete=models.CASCADE,
    )

    class Meta(AbstractAddress.Meta):
        rdf_type = "dfc-b:Address"
        serializer_fields = [
            "@id",
            "address_of",
            "data_server_source",
            "city",
            "country",
            "latitude",
            "longitude",
            "postcode",
            "region",
            "street",
        ]

    def __str__(self):
        return f"{self.address_of} address"


class SocialMedia(AbstractDFCModel):
    enterprise = fields.ForeignKey(
        Enterprise,
        rdf_type="dfc-b:socialMediaOf",
        related_rdf_type="dfc-b:hasSocialMedia",
        blank=True,
        null=True,
        related_name="social_medias",
        on_delete=models.CASCADE,
    )
    name = fields.TextField(
        rdf_type="dfc-b:name",
        blank=True,
        null=True,
    )  # xsd:String
    url = fields.LDPUrlField(
        rdf_type="dfc-b:URL",
        blank=True,
        null=True,
    )

    class Meta(AbstractDFCModel.Meta):
        rdf_type = "dfc-b:SocialMedia"
        serializer_fields = ["@id", "enterprise", "name", "url", "data_server_source"]

    def __str__(self):
        return f"{self.enterprise}: {self.name}"


class Person(AbstractAgent):
    # TODO: a Person is affiliated to an Enterprise via an EnterpriseGroup, not directly?
    # this contradicts the ontology
    affiliated_to = fields.ForeignKey(
        Enterprise,
        rdf_type="dfc-b:affiliatedTo",
        related_rdf_type="dfc-b:affiliates",
        blank=True,
        null=True,
        related_name="affiliates",
        on_delete=models.SET_NULL,
    )
    first_name = fields.TextField(
        rdf_type="dfc-b:firstName",
        blank=True,
        null=True,
    )
    last_name = fields.TextField(
        rdf_type="dfc-b:familyName",
        blank=True,
        null=True,
    )
    # TODO: a person can be the dfc-b:mainContactOf an Enterprise or a PhysicalPlace.
    # This will need to be a generic foreign key (ManyToMany)

    class Meta:
        rdf_type = "dfc-b:Person"
        serializer_fields = [
            "@id",
            "affiliated_to",
            "first_name",
            "last_name",
            "email",
            "logo",
            "logo_url",
            "promo_image_url",
            "phone_number",
            "data_server_source",
        ]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class AbstractProduct(AbstractDFCModel):
    """
    DFC Product ontology: https://lov.linkeddata.es/dataset/lov/vocabs/dfc-p
    In terms of the ontology, an AbstractProduct is a DefinedProduct.

    A DefinedProduct has variations depending on its relationship to the supply line:
    - FunctionalProduct: represents the customers "need".
    - TechnicalProduct: a distributor's proposal to satisfy a customer's need.
    - SuppliedProduct: proposed by a producer to enable distributors to meet their promises to customers.
        It is the implementation of a technical product.
    - LocalizedProduct: a supplied product delivered to a specific locality.
        Therefore, it is NOT a form of product, but rather a relationship between a locality and a product.
    - LocalizedPhysicalProduct: a version of the localized product which has become physical.
        e.g. a potato, once harvested.

    A SuppliedProduct can differ from the TechnicalProduct for example in its implementation, and therefore each form is
    not a "type" of product or a part of the life-cycle of the product, but is indeed a separate model. This is not
    polymorphism.

    In the current version of this package, only SuppliedProducts and LocalizedProducts are implemented and stored,
    but the implementation of other Products is envisaged.
    """

    name = fields.TextField(
        rdf_type="dfc-b:name",
        blank=True,
        null=True,
    )  # xsd:String
    description = fields.TextField(
        rdf_type="dfc-b:description",
        blank=True,
        null=True,
    )
    has_type = fields.CharField(
        rdf_type="dfc-b:hasType",
        verbose_name="has_type",
        choices=ProductType.choices,
        blank=True,
        null=True,
    )
    url = fields.LDPUrlField(
        rdf_type="dfc-b:URL",
        max_length=255,
        blank=True,
        null=True,
    )  # xsd:anyURI

    # TODO: Currently no serialization of reverse in the relationship. Wanted to avoid polymorphism if possible, but a product can be a
    # variant of a product, or a product group, for example
    # dfc-b:hasVariant
    is_variant_of = fields.LDPUrlField(
        rdf_type="dfc-b:isVariantOf",
        max_length=255,
        blank=True,
        null=True,
    )

    # Image
    # has_percentage_of_alcohol_by_volume

    # has_unit
    # referenced_by: CatalogItem
    # concerned_by: OrderLine
    # consumed_by: AsPlannedConsumptionFlow
    # has_process: Process
    # lifetime: literal
    # composes:
    # has_characteristic: PhysicalCharacteristic
    # hasAllergenCharacteristic: PhysicalCharacteristic
    # has_nutrient_characteristic: PhysicalCharacteristic
    # has_ingredient:
    # has_brand: Brand
    # brand: Brand
    # has_certification: Label
    # has_claim: Claim
    # claim: Claim
    # has_container_information:
    # has_geographical_origin: GlobalGenericOrigin
    # has_nature_origin: NatureOrigin
    # has_part_origin: PartOrigin
    # has_labelling_characteristic

    class Meta:
        abstract = True
        rdf_type = "dfc-b:DefinedProduct"


class SuppliedProduct(AbstractProduct):
    """
    A supplied product is proposed by a producer to enable distributors to meet their promises to customers.
    It is the implementation of a technical product.
    """

    supplied_by = fields.ForeignKey(
        Enterprise,
        rdf_type="dfc-b:suppliedBy",
        related_rdf_type="dfc-b:supplies",
        blank=True,
        null=True,
        related_name="supplied_products",
        on_delete=models.SET_NULL,
    )

    # hasQuantity: dfc-b:QuantitativeValue
    # produces: AsPlannedTransformation (via TechnicalProduct)

    class Meta(AbstractProduct.Meta):
        rdf_type = "dfc-b:SuppliedProduct"
        serializer_fields = [
            "@id",
            "name",
            "description",
            "has_type",
            "url",
            "is_variant_of",
            "supplied_by",
        ]
        disable_url = True  # Disables DjangoLDP auto-url generation

    def __str__(self):
        if self.name is not None and len(self.name):
            return f"{self.name} - {self.has_type}"
        return self.urlid


class SuppliedProductGroup(SuppliedProduct):
    """
    Is-a SuppliedProduct, but stored and retrieved separately due to being intended as a collection of SuppliedProducts.
    """

    pass


class LocalizedProduct(AbstractDFCModel):
    """
    A localized product is a supplied product delivered to a specific locality.
    Therefore, it is NOT a form of product, but rather a relationship between a locality and a product.
    """

    reference_of = fields.ForeignKey(
        SuppliedProduct,
        related_rdf_type="dfc-b:hasReference",
        rdf_type="dfc-b:referenceOf",
        blank=True,
        null=True,
        related_name="localized_products",
        on_delete=models.RESTRICT,
    )
    # TODO: foreign key to locality

    class Meta(AbstractDFCModel.Meta):
        rdf_type = "dfc-b:LocalizedProduct"
        serializer_fields = ["@id", "reference_of"]
        disable_url = True  # Disables DjangoLDP auto-url generation

    def __str__(self):
        return f"Localized {self.reference_of}"
