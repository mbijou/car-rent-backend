from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Reservation(models.Model):
    rental_object = models.ForeignKey('rental_objects.RentalObject', null=True, blank=False, on_delete=models.SET_NULL)
    pick_up_datetime = models.DateTimeField()
    return_datetime = models.DateTimeField()

    not_registered_user = models.ForeignKey("users.NotRegisteredUser", null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    car_price_model = models.ForeignKey("price_models.CarPriceModel", null=True, blank=False, on_delete=models.CASCADE)


# 1 NF
# Felder müssen atomar sein: telefon=069432423, 02132143243
# Felder dürfen keine Wiederholungsgruppen haben: telefon1=069432423, telefon2=02132143243
# 2 NF
# Nicht-Schlüsselattribute sind alle voll Funktional abhängig vom Primary Key
# 3 NF
# Nicht-Schlüsselattribute dürfen nicht abhängig von anderen Nicht-Schlüsselattributen sein
