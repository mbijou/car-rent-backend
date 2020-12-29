from rest_framework.test import APITestCase

from manufacturers.api.serializers import ManufacturerSerializer
from manufacturers.models import Manufacturer


class ManufacturerTests(APITestCase):
    def test_manufacturer_can_be_created(self):
        response = self.client.post("/api/v1/manufacturers/", {"name": "BMW"})
        self.assertEqual(response.status_code, 201, "response.status_code should be 201")
        self.assertEqual(Manufacturer.objects.count(), 1, "Manufacturer.objects.count() should be 1")


class SingleManufacturerTests(APITestCase):
    fixtures = ["manufacturers/api/fixtures/manufacturers.json", ]

    def setUp(self):
        self.manufacturer = Manufacturer.objects.get(id=1)

    def test_maufacturer_can_be_updated(self):
        old_name = "BMW"
        self.assertEqual(self.manufacturer.name, old_name, f"self.manufacturer.name should be {old_name}")
        new_name = "Mercedes"

        data = ManufacturerSerializer(instance=self.manufacturer).data
        data["name"] = new_name

        response = self.client.put(f"/api/v1/manufacturers/{self.manufacturer.id}/", data=data)
        self.assertEqual(response.status_code, 200, "response.status_code should be 200")

        self.manufacturer.refresh_from_db()

        self.assertEqual(self.manufacturer.name, new_name, f"self.manufacturer.name should be {new_name}")

    def test_manufacturer_can_be_deleted(self):
        self.assertEqual(Manufacturer.objects.count(), 2, "Manufacturer.objects.count() should be 2")
        response = self.client.delete(f"/api/v1/manufacturers/{self.manufacturer.id}/")
        self.assertEqual(response.status_code, 204, "response.status_code should be 204")
        self.assertEqual(Manufacturer.objects.count(), 1, "Manufacturer.objects.count() should be 1")
