from rest_framework.serializers import ModelSerializer

from rental_objects.models import RentalObject


class RentalObjectSerializer(ModelSerializer):
    class Meta:
        model = RentalObject
        fields = ("id", "car", "year_of_manufacture", "properties", "price_models",)
