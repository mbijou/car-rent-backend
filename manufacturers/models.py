from django.db import models

# Create your models here.


class Manufacturer(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        if self.name:
            return f'{self.name}'
