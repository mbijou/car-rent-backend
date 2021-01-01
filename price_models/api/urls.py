from rest_framework.routers import SimpleRouter
from django.urls import path
from price_models.api.viewsets import PriceModelViewSet, PriceViewSet

router = SimpleRouter()
router.register("price-models", PriceModelViewSet)


prices_urls = [
    path("price-models/<int:price_model_pk>/prices/",
         PriceViewSet.as_view({"get": "list", "post": "create"})),


    path("price-models/<int:price_model_pk>/prices/<int:pk>/",
         PriceViewSet.as_view({"get": "retrieve",
                                         'put': 'update',
                                         'patch': 'partial_update',
                                         'delete': 'destroy',
                                         })),

]


urlpatterns = router.urls + prices_urls
