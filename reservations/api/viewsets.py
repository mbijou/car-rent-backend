from rest_framework.viewsets import ModelViewSet
from reservations.api.serializers import ReservationSerializer
from reservations.models import Reservation


class ReservationModelViewSet(ModelViewSet):
    serializer_class = ReservationSerializer
    queryset = Reservation.objects.all()
