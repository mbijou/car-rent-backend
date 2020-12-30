from rest_framework.viewsets import ModelViewSet

from price_models.api.serializers import PriceModelSerializer, DailyPriceSerializer
from price_models.models import PriceModel, DailyPrice


class PriceModelViewSet(ModelViewSet):
    serializer_class = PriceModelSerializer
    queryset = PriceModel.objects.all()


class DailyPriceModelViewSet(ModelViewSet):
    serializer_class = DailyPriceSerializer
    queryset = DailyPrice.objects.all()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["price_model_pk"] = self.kwargs.get("price_model_pk")
        return context
