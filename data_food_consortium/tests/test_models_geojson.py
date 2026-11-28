from django.contrib.auth import get_user_model
from django.test import TestCase
from djangoldp.models import Model
from rest_framework.test import APIClient

from data_food_consortium.models_geojson import GeoFeature, MultiPoint, Polygon


class TestModelsGeojson(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            username="john",
            email="jlennon@beatles.com",
            password="glass onion",
            is_superuser=True,
        )
        self.client.force_authenticate(self.user)

    def test_geometry_generic_fk_geofeature(self):
        # Feature has a key "geometry" which can be any kind of geometry
        polygon = Polygon.objects.create()
        multi_point = MultiPoint.objects.create(coordinates="Test", polygon=polygon)
        feature = GeoFeature.objects.create()
        feature.geometry = multi_point
        feature.save()

        response = self.client.get(
            Model.resource(feature), content_type="application/ld+json"
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["@id"], feature.urlid)
        self.assertEqual(response.data["geojson:geometry"]["@id"], multi_point.urlid)
        self.assertEqual(
            response.data["geojson:geometry"]["@type"], "geojson:MultiPoint"
        )

        feature.geometry = polygon
        feature.save()
        response = self.client.get(
            Model.resource(feature), content_type="application/ld+json"
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["@id"], feature.urlid)
        self.assertEqual(response.data["geojson:geometry"]["@id"], polygon.urlid)
        self.assertEqual(response.data["geojson:geometry"]["@type"], "geojson:Polygon")
