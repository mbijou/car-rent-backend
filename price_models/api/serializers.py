from django.db.transaction import atomic
from rest_framework import serializers

from price_models.models import PriceModel, DailyPrice


class PriceModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceModel
        fields = ("id", "name", )


class DailyPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyPrice
        fields = ("id", "day", "free_km", "km_price", "fixedprice",)

    @atomic
    def create(self, validated_data):
        price_model_id = self.context.get("price_model_pk")

        instance = DailyPrice(**validated_data)
        instance.price_model_id = price_model_id
        instance.save()
        return instance
