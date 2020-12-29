from rest_framework.test import APITestCase
from cars.models import Car
from cars.api.serializers import CarSerializer


class CarTests(APITestCase):
    fixtures = ['cars/api/fixtures/manufacturers.json', ]

    def test_car_can_be_created(self):
        car_data = {"manufacturer": 1, "type": "car", "model": "X5", }
        response = self.client.post('/api/v1/cars/', car_data, format='json')

        self.assertEqual(response.status_code, 201)
        self.assertEqual(Car.objects.count(), 1, "Car.objects.count() should be 1")


class SingleCarTests(APITestCase):
    fixtures = ['cars/api/fixtures/manufacturers.json', 'cars/api/fixtures/cars.json', ]

    def setUp(self):
        self.car = Car.objects.get(id=3)

    def test_car_can_be_updated(self):
        new_manufacturer_id = 2
        new_model_name = "Tiguan"

        self.assertEqual(self.car.manufacturer_id, 1, "self.car.manufacturer_id should be 1")

        data = CarSerializer(instance=self.car).data

        data["manufacturer"] = new_manufacturer_id
        data["model"] = new_model_name

        response = self.client.put(f"/api/v1/cars/{self.car.id}/", data=data)
        self.assertEqual(response.status_code, 200, "response.status_code should be 200")

        self.car.refresh_from_db()

        self.assertEqual(
            self.car.manufacturer_id, new_manufacturer_id, f"self.car.manufacturer should be {new_manufacturer_id}")

        self.assertEqual(self.car.model, new_model_name, f"self.car.model should be {new_model_name}")

    def test_car_can_be_deleted(self):
        response = self.client.delete(f"/api/v1/cars/{self.car.id}/")
        self.assertEqual(response.status_code, 204, "response.status_code should be 204")
        self.assertEqual(Car.objects.count(), 0, "Car.objects.count() should be 0")


# Move Statement UP: CMD + SHIFT + UP
# Move Statement DOWN: CMD + SHIFT + DOWN

# Python Console: ALT + C
# Run manage.py task: ALT + R

# Auskommentieren: CMD + ALT + 7


# https://realpython.com/django-pytest-fixtures/
