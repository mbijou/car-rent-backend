from django.db import models

# Create your models here.


class Car(models.Model):
    manufacturer = models.ForeignKey('manufacturers.Manufacturer', null=True, blank=False, on_delete=models.SET_NULL)
    type = models.CharField(max_length=200, choices=(("truck", "truck"), ("car", "car"),))
    model = models.CharField(max_length=200)

    price_models = models.ManyToManyField(to="price_models.PriceModel", through="price_models.CarPriceModel")
