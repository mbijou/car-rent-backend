from django.db import models

# Create your models here.


class Property(models.Model):
    name = models.CharField(max_length=200)
    multiple_choice = models.BooleanField(default=False)


class PropertyValue(models.Model):
    value = models.CharField(max_length=200)
