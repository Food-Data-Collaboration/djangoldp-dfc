from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models import Q
from djangoldp import fields

from data_food_consortium.enums import PermissioningScope
from data_food_consortium.fields import GenericForeignKey
from data_food_consortium.models import AbstractDFCModel

"""
GeoJSON models (https://geojson.org/geojson-ld/vocab.html)
GeoJSON format is documented in RFC 7946
"""


class GeoFeatureCollection(AbstractDFCModel):
    class Meta(AbstractDFCModel.Meta):
        rdf_type = "geojson:FeatureCollection"
        serializer_fields = ["@id", "proxy_of", "data_server_source", "features"]
        # TODO: scope could be None instead? Will it break anything?
        dfc_read_scope = PermissioningScope.READ_ENTERPRISE
        dfc_write_scope = PermissioningScope.WRITE_ENTERPRISE

    def __str__(self):
        return ",".join(self.features.values_list("id", flat=True))


class GeoFeature(AbstractDFCModel):
    # Feature has a link to "geometry" which has several concrete types (Point, LineString, Polygon, ...)
    # We use a generic foreign key to achieve this (https://docs.djangoproject.com/en/6.1/ref/contrib/contenttypes/)
    limit = (
        Q(app_label="data_food_consortium", model="point")
        | Q(app_label="data_food_consortium", model="linestring")
        | Q(app_label="data_food_consortium", model="multipoint")
        | Q(app_label="data_food_consortium", model="multilinestring")
        | Q(app_label="data_food_consortium", model="polygon")
        | Q(app_label="data_food_consortium", model="multipolygon")
    )
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        limit_choices_to=limit,
    )
    object_id = models.PositiveIntegerField(null=True)
    collection = fields.ForeignKey(
        GeoFeatureCollection,
        null=True,
        blank=True,
        related_name="features",
        related_rdf_type="geojson:features",
        on_delete=models.SET_NULL,
    )
    geometry = GenericForeignKey(
        "content_type", "object_id", rdf_type="geojson:geometry"
    )
    # NOTE: in future, we could add GenericRelation to geometry concrete types, to access the reverse of geometry
    #   https://docs.djangoproject.com/en/6.1/ref/contrib/contenttypes/#django.contrib.contenttypes.fields.GenericRelation

    class Meta(AbstractDFCModel.Meta):
        rdf_type = "geojson:Feature"
        serializer_fields = ["@id", "proxy_of", "data_server_source", "geometry"]

    def __str__(self):
        return self.urlid


class Point(AbstractDFCModel):
    coordinates = fields.TextField(
        rdf_type="geojson:coordinates", help_text="A single position (RFC 7946)"
    )

    class Meta(AbstractDFCModel.Meta):
        rdf_type = "geojson:Point"
        serializer_fields = ["coordinates"]

    def __str__(self):
        return self.coordinates


class LineString(AbstractDFCModel):
    coordinates = fields.TextField(
        rdf_type="geojson:coordinates",
        help_text="An array of two or more positions (RFC 7946). Stored as a comma separated string",
    )
    multi_line_string = fields.ForeignKey(
        "MultiLineString",
        related_rdf_type="geojson:coordinates",
        related_name="coordinates",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )

    class Meta(AbstractDFCModel.Meta):
        rdf_type = "geojson:LineString"
        serializer_fields = ["@id", "proxy_of", "data_server_source", "coordinates"]

    def __str__(self):
        return self.coordinates

    @property
    def coords(self):
        return self.coordinates.split(",")


class MultiPoint(AbstractDFCModel):
    coordinates = fields.TextField(
        rdf_type="geojson:coordinates",
        help_text="An array of positions (RFC 7946). Stored as a comma separated string",
    )

    polygon = fields.ForeignKey(
        "Polygon",
        related_rdf_type="geojson:coordinates",
        related_name="coordinates",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )

    class Meta(AbstractDFCModel.Meta):
        rdf_type = "geojson:MultiPoint"
        serializer_fields = ["@id", "proxy_of", "data_server_source", "coordinates"]

    def __str__(self):
        return self.coordinates

    @property
    def coords(self):
        return self.coordinates.split(",")


class MultiLineString(AbstractDFCModel):
    """coordinates member is an array of LineString coordinate arrays (RFC 7946)"""

    class Meta(AbstractDFCModel.Meta):
        rdf_type = "geojson:MultiLineString"
        serializer_fields = ["@id", "proxy_of", "data_server_source", "coordinates"]
        nested_fields = ["coordinates"]

    def __str__(self):
        return ", ".join(self.coords)

    @property
    def coords(self):
        return self.coordinates.values_list("coordinates", flat=True)


class Polygon(AbstractDFCModel):
    """Coordinates is an array of linear ring coordinate arrays (RFC 7946)."""

    multi_polygon = fields.ForeignKey(
        "MultiPolygon",
        related_rdf_type="geojson:coordinates",
        related_name="coordinates",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )

    class Meta(AbstractDFCModel.Meta):
        rdf_type = "geojson:Polygon"
        serializer_fields = ["@id", "proxy_of", "data_server_source", "coordinates"]
        nested_fields = ["coordinates"]

    def __str__(self):
        return ", ".join(self.coords)

    @property
    def coords(self):
        return self.coordinates.values_list("coordinates", flat=True)


class MultiPolygon(AbstractDFCModel):
    class Meta(AbstractDFCModel.Meta):
        rdf_type = "geojson:MultiPolygon"
        serializer_fields = ["@id", "proxy_of", "data_server_source", "coordinates"]
        nested_fields = ["coordinates"]

    def __str__(self):
        return ", ".join(self.coordinates.values_list("id", flat=True))


"""
TODO: GeometryCollection has been omitted for now, awaiting multi-model containers
    the main property, "geometries" is an array of geometry objects.
        https://gitlab.com/sib-backup-temp/djangoldp/-/work_items/373
class GeometryCollection(AbstractDFCModel):
    class Meta(AbstractDFCModel.Meta):
        rdf_type = "geojson:GeometryCollection"
        serializer_fields = [
            "@id",
            "proxy_of",
            "data_server_source",
        ]
"""
