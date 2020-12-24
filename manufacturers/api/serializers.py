from rest_framework import serializers

from manufacturers.models import Manufacturer


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ("id", "name", )
