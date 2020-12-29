from rest_framework.viewsets import ModelViewSet

from rental_objects.api.serializers import RentalObjectSerializer
from rental_objects.models import RentalObject


class RentalObjectViewSet(ModelViewSet):
    serializer_class = RentalObjectSerializer
    queryset = RentalObject.objects.all()
