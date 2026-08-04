from django.db import models
from djangoldp import fields
from djangoldp.models import Model
from rdflib import Graph

from data_food_consortium.enums import (
    ProductType,
    ResourceImportSource,
    ShippingOptionType,
    WebhookEventSource,
)
from data_food_consortium.models_common import DataServer


class AbstractDFCModel(Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    data_server_source = fields.ForeignKey(
        DataServer,
        on_delete=models.RESTRICT,
        help_text="The dataserver which provided the instance",
        blank=True,
        null=True,
        rdf_type="dfc-t:dataServerSource",
    )
    proxy_of = fields.TextField(rdf_type="dfc-t:proxyOf", blank=True, null=True)

    class Meta(Model.Meta):
        abstract = True
        serializer_fields = ["@id"]


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
    # NOTE: We use TextField because we don't want to enforce email validation on this data
    email = fields.TextField(
        rdf_type="dfc-b:email",
        blank=True,
        null=True,
    )  # xsd:String
    logo = fields.TextField(
        rdf_type="dfc-b:logo",
        blank=True,
        null=True,
    )  # xsd:anyURI
    logo_url = fields.TextField(rdf_type="ofn:logo_url", blank=True, null=True)
    promo_image_url = fields.TextField(
        rdf_type="ofn:promo_image_url", blank=True, null=True
    )
    phone_number = fields.TextField(
        rdf_type="dfc-b:hasPhoneNumber",
        blank=True,
        null=True,
    )
    website_page = fields.TextField(
        rdf_type="dfc-b:websitePage",
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
        depth = 10
        serializer_fields = [
            "@id",
            "proxy_of",
            "data_server_source",
            "name",
            "email",
            "logo",
            "logo_url",
            "promo_image_url",
            "phone_number",
            "website_page",
            "description",
            "long_description",
            "contact_name",
            "VATnumber",
            "VATstatus",
            "addresses",
            "social_medias",
            "supplied_products",
            "affiliated_to",
            "catalog_items",
            "services",
            "coordinations",
            "customer_categories",
            "shipping_options",
        ]
        nested_fields = [
            "addresses",
            "social_medias",
            "supplied_products",
            "affiliated_to",
            "catalog_items",
            "services",
            "coordinations",
            "shipping_options",
        ]
        disable_url = True  # Disables DjangoLDP auto-url generation

    def __str__(self):
        return self.urlid

    # defines = models.TextField(blank=True, null=True) # Reverse on CustomerCategory model
    # maintains = models.TextField(blank=True, null=True) reverse on Catalog
    # orders = models.TextField(blank=True, null=True) from subclassing Agent. Reverse on Orders
    # owns = models.TextField(blank=True, null=True) from subclassing Agent. Reverse on Brand
    # sells = models.TextField(blank=True, null=True) FK to model Order
    # transforms = models.TextField(blank=True, null=True) FK to model "as planned local transformation"

    @classmethod
    def serializer_class(cls):
        from data_food_consortium.serializers import EnterpriseSerializer

        return EnterpriseSerializer


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
            "proxy_of",
            "data_server_source",
            "city",
            "country",
            "latitude",
            "longitude",
            "postcode",
            "region",
            "street",
        ]
        container_path = "enterprise_addresses"

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
    url = fields.TextField(
        rdf_type="dfc-b:URL",
        blank=True,
        null=True,
    )

    class Meta(AbstractDFCModel.Meta):
        rdf_type = "dfc-b:SocialMedia"
        serializer_fields = ["@id", "proxy_of", "data_server_source", "name", "url"]
        container_path = "social_medias"

    def __str__(self):
        return f"{self.enterprise}: {self.name}"


class Person(AbstractAgent):
    affiliates = fields.ForeignKey(
        Enterprise,
        rdf_type="dfc-b:affiliates",
        related_rdf_type="dfc-b:affiliatedTo",
        blank=True,
        null=True,
        related_name="affiliated_to",
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
            "proxy_of",
            "data_server_source",
            "first_name",
            "last_name",
            "email",
            "logo",
            "logo_url",
            "promo_image_url",
            "phone_number",
            "places",
        ]
        nested_fields = ["affiliates", "places"]

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
    image = fields.TextField(
        rdf_type="dfc-b:image",
        blank=True,
        null=True,
    )
    has_type = fields.CharField(
        rdf_type="dfc-b:hasType",
        verbose_name="has_type",
        choices=ProductType.choices,
        blank=True,
        null=True,
        max_length=255,
    )
    url = fields.TextField(
        rdf_type="dfc-b:URL",
        max_length=255,
        blank=True,
        null=True,
    )  # xsd:anyURI
    specific_condition = fields.TextField(
        rdf_type="dfc-b:specificCondition",
        null=True,
        blank=True,
        help_text="Any specific conditions requried for storage or carriage of the Product.",
    )

    # TODO: has_unit (dfc-b:hasUnit): a dfc-m:Unit value

    # TODO: Currently no serialization of reverse in the relationship. Wanted to avoid polymorphism if possible, but a product can be a
    # variant of a product, or a product group, for example
    # dfc-b:hasVariant
    is_variant_of = fields.LDPUrlField(
        rdf_type="dfc-b:isVariantOf",
        max_length=255,
        blank=True,
        null=True,
    )

    has_ingredient = fields.JSONField(
        rdf_type="dfc-b:hasIngredient", blank=True, null=True
    )

    # has_percentage_of_alcohol_by_volume
    # concerned_by: OrderLine
    # consumed_by: AsPlannedConsumptionFlow
    # has_process: Process
    # lifetime: literal
    # composes:
    # has_characteristic: PhysicalCharacteristic
    # hasAllergenCharacteristic: PhysicalCharacteristic
    # has_nutrient_characteristic: PhysicalCharacteristic
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

    @classmethod
    def serializer_class(cls):
        from data_food_consortium.serializers import ProductSerializer

        return ProductSerializer


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
            "proxy_of",
            "data_server_source",
            "name",
            "description",
            "has_type",
            "image",
            "url",
            "is_variant_of",
        ]
        disable_url = True  # Disables DjangoLDP auto-url generation
        container_path = "supplied_products"

    def __str__(self):
        if self.name is not None and len(self.name):
            return f"{self.name} - {self.has_type}"
        return self.urlid


class SuppliedProductGroup(SuppliedProduct):
    """
    Is-a SuppliedProduct, but stored and retrieved separately due to being intended as a collection of SuppliedProducts.
    """


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
        serializer_fields = ["@id", "proxy_of", "data_server_source", "reference_of"]
        disable_url = True  # Disables DjangoLDP auto-url generation

    def __str__(self):
        return f"Localized {self.reference_of}"


class CatalogItem(AbstractDFCModel):
    """
    A CatalogItem is a product, listed for sale.
    """

    managed_by = fields.ForeignKey(
        Enterprise,
        related_rdf_type="dfc-b:manages",
        rdf_type="dfc-b:managedBy",
        blank=True,
        null=True,
        related_name="catalog_items",
        on_delete=models.CASCADE,
    )
    # TODO: "references" should be a ForeignKey to any DefinedProduct implementation
    #   https://git.startinblox.com/djangoldp-packages/djangoldp/-/issues/446
    references = fields.ForeignKey(
        SuppliedProduct,
        related_rdf_type="dfc-b:referencedBy",
        rdf_type="dfc-b:references",
        blank=True,
        null=True,
        related_name="referenced_by",
        on_delete=models.CASCADE,
    )

    extra_availability_time = fields.TextField(
        blank=True, null=True, rdf_type="dfc-b:extraAvailabilityTime"
    )  # xsd:duration
    extra_delivery_condition = fields.TextField(
        blank=True, null=True, rdf_type="dfc-b:extraDeliveryCondition"
    )
    sku = fields.TextField(blank=True, null=True, rdf_type="dfc-b:sku")
    stock_limitation = fields.FloatField(
        blank=True, null=True, rdf_type="dfc-b:stockLimitation"
    )

    class Meta:
        rdf_type = "dfc-b:CatalogItem"
        serializer_fields = [
            "@id",
            "proxy_of",
            "data_server_source",
            "references",
            "extra_availability_time",
            "extra_delivery_condition",
            "sku",
            "stock_limitation",
            "offers",
        ]
        nested_fields = ["offers"]
        container_path = "catalog_items"

    def __str__(self):
        return f"CatalogItem {self.references} ({self.managed_by})"


class CustomerCategory(AbstractDFCModel):
    name = fields.TextField(
        rdf_type="dfc-b:name",
        blank=True,
        null=True,
    )
    defined_by = fields.ForeignKey(
        Enterprise,
        related_rdf_type="dfc-b:defines",
        rdf_type="dfc-b:definedBy",
        blank=True,
        null=True,
        related_name="customer_categories",
        on_delete=models.CASCADE,
    )

    class Meta:
        rdf_type = "dfc-b:CustomerCategory"
        serializer_fields = ["@id", "proxy_of", "data_server_source", "name", "offers"]
        nested_fields = ["offers"]
        container_path = "customer_categories"

    def __str__(self):
        return f"CatalogItem {self.id}"


class Price(AbstractDFCModel):
    value = fields.FloatField(blank=True, null=True, rdf_type="dfc-b:value")
    # TODO: hasUnit should point to an RDF value and we could add a custom constraint for this.
    has_unit = fields.TextField(blank=True, null=True, rdf_type="dfc-b:hasUnit")

    class Meta:
        rdf_type = "dfc-b:Price"
        serializer_fields = [
            "@id",
            "proxy_of",
            "data_server_source",
            "value",
            "has_unit",
        ]

    def __str__(self):
        return f"Price {self.value} ({self.has_unit})"


class Offer(AbstractDFCModel):
    offers = fields.ForeignKey(
        CatalogItem,
        related_rdf_type="dfc-b:offeredThrough",
        rdf_type="dfc-b:offers",
        blank=True,
        null=True,
        related_name="offers",
        on_delete=models.CASCADE,
    )
    offered_to = fields.ForeignKey(
        CustomerCategory,
        related_rdf_type="dfc-b:offers",
        rdf_type="dfc-b:offeredTo",
        blank=True,
        null=True,
        related_name="offers",
        on_delete=models.CASCADE,
    )
    offered_for = fields.ForeignKey(
        Price,
        related_rdf_type="dfc-b:priceOf",
        rdf_type="dfc-b:hasPrice",
        blank=True,
        null=True,
        related_name="offers",
        on_delete=models.RESTRICT,
    )
    discount = fields.FloatField(blank=True, null=True, rdf_type="dfc-b:discount")
    stock_limitation = fields.FloatField(
        blank=True, null=True, rdf_type="dfc-b:stockLimitation"
    )

    class Meta:
        rdf_type = "dfc-b:Offer"
        serializer_fields = ["@id", "proxy_of", "data_server_source", "offered_for"]

    def __str__(self):
        return f"Offer of {self.offers} to {self.offered_to} for {self.offered_for}"


class Service(AbstractDFCModel):
    """
    Represents a service that can be provided by an Enterprise, like "home delivery".

    NOTE: This model isn't currently a part of the DFC standard, and was added early
    for the CQCM use-case. To reflect this, it uses the CQCM namespace for now. When it is
    added to the DFC standard, the namespace should be replaced and data migrated.
    """

    name = fields.TextField(
        rdf_type="dfc-b:name",
        blank=True,
        null=True,
    )

    class Meta:
        rdf_type = "cqcm:Service"
        serializer_fields = [
            "@id",
            "proxy_of",
            "data_server_source",
            "created_at",
            "updated_at",
            "name",
        ]
        nested_fields = ["suppliers"]

    def __str__(self):
        return self.name


class EnterpriseService(AbstractDFCModel):
    enterprise = fields.ForeignKey(
        Enterprise,
        rdf_type="dfc-b:suppliedBy",
        related_rdf_type="cqcm:services",
        blank=True,
        null=True,
        related_name="services",
        on_delete=models.CASCADE,
    )
    service = fields.ForeignKey(
        Service,
        rdf_type="cqcm:supplies",
        related_rdf_type="cqcm:suppliers",
        blank=True,
        null=True,
        related_name="suppliers",
        on_delete=models.RESTRICT,
    )

    class Meta:
        rdf_type = "cqcm:EnterpriseService"
        serializer_fields = [
            "@id",
            "proxy_of",
            "data_server_source",
            "created_at",
            "updated_at",
            "service",
        ]
        container_path = "enterprise_services"

    def __str__(self):
        return f"{self.service.name} ({self.enterprise})"


class PhysicalPlaceAddress(AbstractAddress):
    class Meta(AbstractAddress.Meta):
        rdf_type = "dfc-b:Address"
        serializer_fields = [
            "@id",
            "proxy_of",
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
        return self.urlid


class PhysicalPlace(AbstractDFCModel):
    name = fields.TextField(
        rdf_type="dfc-b:name",
        blank=True,
        null=True,
    )
    address = fields.ForeignKey(
        PhysicalPlaceAddress,
        related_rdf_type="dfc-b:addressOf",
        rdf_type="dfc-b:hasAddress",
        blank=True,
        null=True,
        related_name="places",
        on_delete=models.SET_NULL,
    )
    main_contact = fields.ForeignKey(
        Person,
        related_rdf_type="dfc-b:mainContactOf",
        rdf_type="dfc-b:hasMainContact",
        blank=True,
        null=True,
        related_name="places",
        on_delete=models.SET_NULL,
    )
    phone_number = fields.TextField(
        rdf_type="dfc-b:hasPhoneNumber",
        blank=True,
        null=True,
    )
    URL = fields.TextField(rdf_type="dfc-b:URL", blank=True, null=True)

    class Meta:
        rdf_type = "dfc-b:PhysicalPlace"
        serializer_fields = [
            "proxy_of",
            "data_server_source",
            "name",
            "address",
            "main_contact",
            "phone_number",
            "URL",
        ]

    def __str__(self):
        return self.name if self.name and len(self.name) else str(self.address)


class Coordination(AbstractDFCModel):
    """
    A descriptor giving the coordinator of a Sales Session
    and the percentage margin taken by the coordinator to manage the sale session.
    """

    name = fields.TextField(
        rdf_type="dfc-b:name",
        blank=True,
        null=True,
    )
    enterprise = fields.ForeignKey(
        Enterprise,
        rdf_type="dfc-b:coordinates",
        related_rdf_type="dfc-b:coordinatedBy",
        blank=True,
        null=True,
        related_name="coordinations",
        on_delete=models.CASCADE,
        help_text=(
            "Confirms the Enterprise Coordinates certain SaleSessions, "
            "and defines margin percentage that the Enterprise takes for managing the SaleSession"
        ),
    )
    margin_percent = fields.FloatField(
        blank=True,
        null=True,
        rdf_type="dfc-b:marginPercent",
        default=0.0,
        help_text=(
            "The percentage margin the coordinating Enterprise is charging as comission "
            "for managing the Sales Session (from 0-100)"
        ),
    )

    class Meta:
        rdf_type = "dfc-b:Coordination"
        serializer_fields = [
            "@id",
            "proxy_of",
            "data_server_source",
            "name",
            "margin_percent",
            "sale_sessions",
        ]
        nested_fields = ["sale_sessions"]

    def __str__(self):
        return f"{self.name} ({self.enterprise})"


class SaleSession(AbstractDFCModel):
    """
    Time bounded grouping of Offers for an Enterprise.
    """

    coordination = fields.ForeignKey(
        Coordination,
        rdf_type="dfc-b:objectOf",
        related_rdf_type="dfc-b:hasObject",
        help_text="The Coordination (that defines which Enterprise coordinates the Sales Sesison)",
        blank=True,
        null=True,
        related_name="sale_sessions",
        on_delete=models.CASCADE,
    )
    hosted_at = fields.ForeignKey(
        PhysicalPlace,
        rdf_type="dfc-b:hostedAt",
        related_rdf_type="dfc-b:hosts",
        blank=True,
        null=True,
        related_name="sale_sessions",
        on_delete=models.SET_NULL,
    )

    quantity = fields.FloatField(blank=True, null=True, rdf_type="dfc-b:quantity")
    start_date = fields.DateTimeField(rdf_type="dfc-b:startDate", blank=True, null=True)
    end_date = fields.DateTimeField(rdf_type="dfc-b:endDate", blank=True, null=True)

    class Meta:
        rdf_type = "dfc-b:SaleSession"
        serializer_fields = [
            "@id",
            "proxy_of",
            "data_server_source",
            "start_date",
            "end_date",
            "quantity",
            "hosted_at",
            "shipping_options",
        ]
        nested_fields = ["shipping_options"]

    def __str__(self):
        return f"{self.coordination} ({self.start_date} - {self.end_date})"


class ShippingOption(AbstractDFCModel):
    """
    Pick-up options and Delivery options are available to the customer of a SaleSession.
    """

    enterprise = fields.ForeignKey(
        Enterprise,
        rdf_type="cqcm:optionOf",
        related_rdf_type="cqcm:shippingOptions",
        blank=True,
        null=True,
        related_name="shipping_options",
        on_delete=models.CASCADE,
        help_text="Automatically set to the enterprise coordinating the SaleSession. Not part of the DFC standard",
    )
    sale_session = fields.ForeignKey(
        SaleSession,
        rdf_type="dfc-b:optionOf",
        related_rdf_type="dfc-b:hasOption",
        blank=True,
        null=True,
        related_name="shipping_options",
        on_delete=models.CASCADE,
    )
    delivers_at = fields.ForeignKey(
        PhysicalPlace,
        rdf_type="dfc-b:deliversAt",
        related_rdf_type="dfc-b:deliveries",
        blank=True,
        null=True,
        related_name="deliveries",
        on_delete=models.SET_NULL,
    )
    picked_up_at = fields.ForeignKey(
        PhysicalPlace,
        rdf_type="dfc-b:pickedUpAt",
        related_rdf_type="dfc-b:collections",
        blank=True,
        null=True,
        related_name="collections",
        on_delete=models.SET_NULL,
    )

    has_type = fields.CharField(
        choices=ShippingOptionType.choices,
        blank=True,
        null=True,
        max_length=255,
    )
    fee = fields.FloatField(blank=True, null=True, rdf_type="dfc-b:fee")
    quantity = fields.FloatField(blank=True, null=True, rdf_type="dfc-b:quantity")
    start_date = fields.DateTimeField(rdf_type="dfc-b:startDate", blank=True, null=True)
    end_date = fields.DateTimeField(rdf_type="dfc-b:endDate", blank=True, null=True)

    class Meta:
        rdf_type = "dfc-b:ShippingOption"
        serializer_fields = [
            "@id",
            "proxy_of",
            "data_server_source",
            "has_type",
            "fee",
            "quantity",
            "start_date",
            "end_date",
            "delivers_at",
            "picked_up_at",
        ]

    def __str__(self):
        return f"{self.urlid} ({self.sale_session})"

    def save(self, *args, **kwargs):
        if (
            self.sale_session
            and self.sale_session.coordination
            and self.sale_session.coordination.enterprise
        ):
            self.enterprise = self.sale_session.coordination.enterprise
        return super().save(*args, **kwargs)


class ResourceImportRecord(models.Model):
    """
    A report corresponding to an import of data onto this proxy (e.g. via webhook or import command)
    Only stored if these reports are configured in settings.
    """

    created_at = models.DateTimeField(auto_now_add=True)
    import_started_at = models.DateTimeField()
    data_batches = fields.JSONField(
        blank=True,
        null=True,
        help_text="A list of the JSON data received from the data-server, received in batches",
    )
    data_server_source = fields.TextField(blank=True, null=True)
    imported_models = fields.TextField(
        blank=True,
        null=True,
        help_text="The models which were imported based on the webhook data",
    )
    imported_subjects = fields.TextField(
        blank=True, null=True, help_text="The instances found in the data"
    )
    deleted_subjects = fields.TextField(
        blank=True,
        null=True,
        help_text="Instances which were discarded as a result of the import, e.g. if permission was removed",
    )
    source = fields.CharField(
        choices=ResourceImportSource.choices,
        blank=True,
        null=True,
        max_length=64,
        help_text="How the import was triggered (e.g. via the command line or webhook)",
    )

    def __str__(self):
        return f"{self.data_server_source} ({self.import_started_at})"

    @property
    def parsed_data(self):
        result = []
        for data_batch in self.data_batches:
            graph = Graph()
            graph.parse(data=data_batch, format="json-ld")
            result.append(graph.serialize(format="json-ld"))
        return result


class RevokeWebhookRecord(models.Model):
    completed_at = models.DateTimeField(auto_now_add=True)
    data = fields.JSONField(
        blank=True, null=True, help_text="The JSON data sent with the webhook"
    )
    platform_urlid = fields.TextField(
        blank=True, null=True, help_text="The platform which sent the webhook"
    )
    source = fields.CharField(
        choices=WebhookEventSource.choices,
        blank=True,
        null=True,
        max_length=64,
        help_text="How the webhook was triggered",
    )

    def __str__(self):
        return f"{self.platform_urlid} ({self.completed_at})"
