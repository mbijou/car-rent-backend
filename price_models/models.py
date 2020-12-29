from django.db import models

# Create your models here.


class PriceModel(models.Model):
    free_km = models.IntegerField()
    over_free_km_price = models.DecimalField(max_digits=8, decimal_places=2)  # ct./ km
    fixedprice = models.DecimalField(max_digits=8, decimal_places=2)

    rental_objects = models.ManyToManyField(to="rental_objects.RentalObject",
                                            through='price_models.RentalObjectPriceModel')


DAYS_OF_WEEK = (
    (1, 'Monday'),
    (2, 'Tuesday'),
    (3, 'Wednesday'),
    (4, 'Thursday'),
    (5, 'Friday'),
    (6, 'Saturday'),
    (7, 'Sunday'),
)


class RentalObjectPriceModel(models.Model):
    price_model = models.ForeignKey("price_models.PriceModel", null=True, blank=False, on_delete=models.CASCADE)
    rental_object = models.ForeignKey("rental_objects.RentalObject", null=True, blank=False, on_delete=models.CASCADE)
    day = models.CharField(max_length=1, choices=DAYS_OF_WEEK)
