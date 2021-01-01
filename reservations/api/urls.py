from rest_framework.routers import SimpleRouter

from reservations.api.viewsets import ReservationModelViewSet

router = SimpleRouter()
router.register("reservations", ReservationModelViewSet)

urlpatterns = router.urls
