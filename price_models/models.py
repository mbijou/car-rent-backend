from django.db import models

# Create your models here.


class PriceModel(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)


DAYS_OF_WEEK = (
    (1, 'Monday'),
    (2, 'Tuesday'),
    (3, 'Wednesday'),
    (4, 'Thursday'),
    (5, 'Friday'),
    (6, 'Saturday'),
    (7, 'Sunday'),
)


class Price(models.Model):
    price_model = models.ForeignKey("price_models.PriceModel", on_delete=models.CASCADE)
    day = models.IntegerField(choices=DAYS_OF_WEEK)
    free_km = models.IntegerField()
    km_price = models.DecimalField(max_digits=8, decimal_places=2)  # ct./ km
    fixedprice = models.DecimalField(max_digits=8, decimal_places=2)
