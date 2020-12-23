from rest_framework.routers import SimpleRouter
from cars.api.viewsets import CarViewSet


router = SimpleRouter()
router.register("cars", CarViewSet)

urlpatterns = router.urls
