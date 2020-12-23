from django.db import models

# Create your models here.


class Car(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200, choices=(("truck", "truck"), ("car", "car"),))
    model = models.CharField(max_length=200)
    year_of_manufacture = models.DateField()
