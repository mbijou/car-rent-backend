from rest_framework.routers import SimpleRouter

from rental_objects.api.viewsets import RentalObjectViewSet

router = SimpleRouter()
router.register("rental-objects", RentalObjectViewSet)

urlpatterns = router.urls
