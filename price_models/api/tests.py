from rest_framework.test import APITestCase

from price_models.api.serializers import PriceModelSerializer, DailyPriceSerializer
from price_models.models import PriceModel, DailyPrice


class PriceModelTests(APITestCase):
    def test_price_model_can_be_created(self):
        price_model_name = "A"
        data = {"name": price_model_name}
        response = self.client.post("/api/v1/price-models/", data=data)
        self.assertEqual(response.status_code, 201, "response.status_code should be 201")
        self.assertEqual(PriceModel.objects.count(), 1, "PriceModel.objects.count() should be 1")
        price_model = PriceModel.objects.first()
        self.assertEqual(price_model.name, price_model_name, f"price_model.name should be {price_model_name}")


class SinglePriceModelTests(APITestCase):
    fixtures = ["price_models/api/fixtures/price_models.json", ]

    def setUp(self):
        self.price_model = PriceModel.objects.get(pk=1)

    def test_price_model_can_be_updated(self):
        new_price_model_name = "B"
        self.assertNotEqual(self.price_model, new_price_model_name,
                            f"self.price_model should not be {new_price_model_name}")
        data = PriceModelSerializer(instance=self.price_model).data
        data["name"] = new_price_model_name

        response = self.client.put(f"/api/v1/price-models/{self.price_model.id}/", data=data)
        self.assertEqual(response.status_code, 200, "response.status_code should be 200")

        self.price_model.refresh_from_db()
        self.assertEqual(self.price_model.name, new_price_model_name,
                         f"self.price_model.name should be {new_price_model_name}")

    def test_price_model_can_be_deleted(self):
        self.assertEqual(PriceModel.objects.count(), 2, "PriceModel.objects.count() should be 2")
        response = self.client.delete(f"/api/v1/price-models/{self.price_model.id}/")
        self.assertEqual(response.status_code, 204, "response.status_code should be 204")
        self.assertEqual(PriceModel.objects.count(), 1, "PriceModel.objects.count() should be 1")


class DailyPriceTests(APITestCase):
    fixtures = ["price_models/api/fixtures/price_models.json", ]

    def setUp(self):
        self.price_model = PriceModel.objects.get(pk=1)

    def test_daily_price_can_be_created(self):
        data = {"day": 1, "free_km": 200, "km_price": 0.19, "fixedprice": 30}
        response = self.client.post(f"/api/v1/price-models/{self.price_model.id}/daily-prices/", data=data)

        self.assertEqual(response.status_code, 201, "response.status_code should be 201")
        self.assertEqual(DailyPrice.objects.count(), 1, "DailyPrice.objects.count() should be 1")
        daily_price_instance = DailyPrice.objects.get(price_model=self.price_model)
        self.assertEqual(daily_price_instance.price_model_id, self.price_model.id,
                         f"daily_price_instance.price_model_id should be {self.price_model.id}")


class SingleDailyPriceTests(APITestCase):
    fixtures = ["price_models/api/fixtures/price_models.json", "price_models/api/fixtures/daily_prices.json", ]

    def setUp(self):
        self.price_model = PriceModel.objects.get(pk=2)
        self.daily_price = DailyPrice.objects.get(pk=1)

    def test_daily_price_can_be_updated(self):
        new_day, new_free_km, new_km_price, new_fixedprice = 2, 700, 0.5, 200

        data = DailyPriceSerializer(instance=self.daily_price).data

        data["day"], data["free_km"], data["km_price"], data["fixedprice"] = \
            new_day, new_free_km, new_km_price, new_fixedprice

        response = self.client.put(f"/api/v1/price-models/{self.price_model.id}/daily-prices/{self.daily_price.pk}/",
                                   data=data)

        self.assertEqual(response.status_code, 200, "response.status_code should be 200")

        self.daily_price.refresh_from_db()

        self.assertEqual(self.daily_price.day, new_day)
        self.assertEqual(self.daily_price.free_km, new_free_km)
        self.assertEqual(self.daily_price.km_price, new_km_price)
        self.assertEqual(self.daily_price.fixedprice, new_fixedprice)

    def test_daily_price_can_be_deleted(self):
        self.assertEqual(DailyPrice.objects.count(), 1, "DailyPrice.objects.count() should be 1")
        response = self.client.delete(
            f"/api/v1/price-models/{self.price_model.id}/daily-prices/{self.daily_price.pk}/"
        )
        self.assertEqual(response.status_code, 204, "response.status_code should be 204")
        self.assertEqual(DailyPrice.objects.count(), 0, "DailyPrice.objects.count() should be 0")
