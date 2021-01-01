from django.db.transaction import atomic
from rest_framework import serializers
from reservations.models import Reservation
from users.api.serializers import NotRegisteredUserSerializer
from users.models import NotRegisteredUser, Address


class ReservationSerializer(serializers.ModelSerializer):
    not_registered_user = NotRegisteredUserSerializer()

    class Meta:
        model = Reservation
        fields = ("id", "rental_object", "pick_up_datetime", "return_datetime", "not_registered_user", "user",
                  "price", )

    @atomic
    def create(self, validated_data):
        not_registered_user_data = validated_data.pop("not_registered_user")

        profile_data = not_registered_user_data.pop("profile")

        address_data = profile_data.pop("address")
        address = Address(**address_data)
        address.save()

        not_registered_user = NotRegisteredUser(**not_registered_user_data)
        not_registered_user.save()

        not_registered_user.profile.address = address
        not_registered_user.save()

        reservation = Reservation(**validated_data, not_registered_user=not_registered_user)
        reservation.save()
        return reservation
