from rest_framework.viewsets import ModelViewSet

from price_models.api.serializers import PriceModelSerializer, PriceSerializer
from price_models.models import PriceModel, Price


class PriceModelViewSet(ModelViewSet):
    serializer_class = PriceModelSerializer
    queryset = PriceModel.objects.all()


class PriceViewSet(ModelViewSet):
    serializer_class = PriceSerializer
    queryset = Price.objects.all()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["price_model_pk"] = self.kwargs.get("price_model_pk")
        return context
