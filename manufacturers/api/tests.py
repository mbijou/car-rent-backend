from rest_framework.test import APITestCase

from manufacturers.models import Manufacturer


class ManufacturerTests(APITestCase):
    def test_manufacturer_can_be_created(self):
        response = self.client.post("/api/v1/manufacturers/", {"name": "BMW"})
        self.assertEqual(response.status_code, 201, "response.status_code should be 201")
        self.assertEqual(Manufacturer.objects.count(), 1, "Manufacturer.objects.count() should be 1")
