from django.db import models

# Create your models here.


class PriceModel(models.Model):
    free_km = models.IntegerField()
    over_free_km_price = models.DecimalField(max_digits=8, decimal_places=2)  # ct./ km
    fixedprice = models.DecimalField(max_digits=8, decimal_places=2)

    cars = models.ManyToManyField(to="cars.Car", through='price_models.CarPriceModel')


DAYS_OF_WEEK = (
    (1, 'Monday'),
    (2, 'Tuesday'),
    (3, 'Wednesday'),
    (4, 'Thursday'),
    (5, 'Friday'),
    (6, 'Saturday'),
    (7, 'Sunday'),
)


class CarPriceModel(models.Model):
    price_model = models.ForeignKey("price_models.PriceModel", on_delete=models.CASCADE)
    car = models.ForeignKey("cars.Car", on_delete=models.CASCADE)
    days = models.CharField(max_length=1, choices=DAYS_OF_WEEK)
