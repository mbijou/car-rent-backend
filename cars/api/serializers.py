from rest_framework import serializers
from cars.models import Car


class CarSerializer(serializers.ModelSerializer):
    manufacturer_name = serializers.CharField(read_only=True, source="manufacturer")

    class Meta:
        model = Car
        fields = ("id", "manufacturer_name", "manufacturer", "type", "model", "year_of_manufacture",)
