import copy

from django.conf import settings
from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.test import APIClient

from data_food_consortium.models import Enterprise
from data_food_consortium.utils import get_serializer_class


class TestOntologyFlexibility(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            username="john", email="jlennon@beatles.com", password="glass onion"
        )
        self.client.force_authenticate(self.user)

    def test_enterprise_ontology_v1(self):
        """Can POST data in ontology v1, receive it in V2"""
        data = {
            "@context": settings.LDP_RDF_CONTEXT_V1,
            "@type": "dfc-b:Enterprise",
            "dfc-b:name": "Fred's Farm",
            "dfc-b:hasAddress": {
                "@type": "ldp:Container",
                "ldp:contains": [
                    {
                        "dfc-b:hasCity": "Herndon",
                        "dfc-b:hasCountry": "Australia",
                        "dfc-b:hasPostalCode": "20170",
                        "dfc-b:region": "Victoria",
                        "dfc-b:hasStreet": "42 Doveton Street",
                        "@type": "dfc-b:Address",
                    }
                ],
            },
        }
        v1_address = copy.deepcopy(data["dfc-b:hasAddress"]["ldp:contains"][0])

        serializer = get_serializer_class(Enterprise)(data=data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()

        response = self.client.get(instance.urlid)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["@type"], "dfc-b:Organization")
        v2_address = response.data["dfc-b:hasAddress"]["ldp:contains"][0]
        self.assertEqual(v2_address["dfc-b:city"], v1_address["dfc-b:hasCity"])
        self.assertEqual(
            v2_address["dfc-b:postcode"], v1_address["dfc-b:hasPostalCode"]
        )
        self.assertEqual(v2_address["dfc-b:street"], v1_address["dfc-b:hasStreet"])
