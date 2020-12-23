from rest_framework import serializers
from cars.models import Car


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ("id", "name", "type", "model", "year_of_manufacture",)