from rest_framework.viewsets import ModelViewSet
from cars.api.serializers import CarSerializer
from cars.models import Car


class CarViewSet(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
