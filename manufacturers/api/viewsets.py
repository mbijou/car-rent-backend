from rest_framework.viewsets import ModelViewSet

from manufacturers.api.serializers import ManufacturerSerializer
from manufacturers.models import Manufacturer


class ManufacturerViewSet(ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
