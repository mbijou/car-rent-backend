from rest_framework.test import APITestCase

from rental_objects.api.serializers import RentalObjectSerializer
from rental_objects.models import RentalObject


class RentalObjectTests(APITestCase):
    fixtures = ['rental_objects/api/fixtures/manufacturers.json', 'rental_objects/api/fixtures/cars.json',
                'rental_objects/api/fixtures/price_models.json'
                ]

    def test_rental_object_can_be_created(self):
        data = {"car": 1, "year_of_manufacture": 2020, "price_model": 1}
        response = self.client.post("/api/v1/rental-objects/", data=data)
        self.assertEqual(response.status_code, 201, "response.status_code should be 201")
        self.assertEqual(RentalObject.objects.count(), 1, "RentalObject.objects.count()")


class SingleRentalObjectTests(APITestCase):
    fixtures = ['rental_objects/api/fixtures/manufacturers.json', 'rental_objects/api/fixtures/cars.json',
                'rental_objects/api/fixtures/price_models.json', 'rental_objects/api/fixtures/rental_objects.json', ]

    def setUp(self):
        self.rental_object = RentalObject.objects.get(id=1)

    def test_rental_object_can_be_updated(self):
        new_car_id = 2
        new_price_model_id = 1

        serializer = RentalObjectSerializer(instance=self.rental_object)

        data = serializer.data

        data["car"] = new_car_id
        data["price_model"] = new_price_model_id

        response = self.client.put(f"/api/v1/rental-objects/{self.rental_object.id}/", data=data)
        self.assertEqual(response.status_code, 200, "response.status_code should be 200")

        self.rental_object.refresh_from_db()

        self.assertEqual(
            self.rental_object.car_id, new_car_id, f"rental_object.car_id should be {new_car_id}")

        self.assertEqual(
            self.rental_object.price_model_id, new_price_model_id,
            f"rental_object.price_model_id should be {new_price_model_id}")

    def test_rental_object_can_be_deleted(self):
        self.assertEqual(RentalObject.objects.count(), 1, "RentalObject.objects.count() should be 1")
        response = self.client.delete(f"/api/v1/rental-objects/{self.rental_object.id}/")
        self.assertEqual(response.status_code, 204, "response.status_code should be 204")
        self.assertEqual(RentalObject.objects.count(), 0, "RentalObject.objects.count() shoud be 0")
