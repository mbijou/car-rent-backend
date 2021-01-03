from django.db import models

# Create your models here.


class RentalObject(models.Model):
    car = models.ForeignKey('cars.Car', null=True, blank=False, on_delete=models.SET_NULL)

    properties = models.ManyToManyField('properties.PropertyValue', blank=True)
    price_models = models.ManyToManyField("price_models.PriceModel", blank=True)

    year_of_manufacture = models.IntegerField()
