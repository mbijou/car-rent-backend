from rest_framework.routers import SimpleRouter

from manufacturers.api.viewsets import ManufacturerViewSet

router = SimpleRouter()

router.register('manufacturers', ManufacturerViewSet)

urlpatterns = router.urls
