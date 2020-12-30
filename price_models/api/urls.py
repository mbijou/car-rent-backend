from rest_framework.routers import SimpleRouter
from django.urls import path
from price_models.api.viewsets import PriceModelViewSet, DailyPriceModelViewSet

router = SimpleRouter()
router.register("price-models", PriceModelViewSet)


daily_prices_urls = [
    path("price-models/<int:price_model_pk>/daily-prices/",
         DailyPriceModelViewSet.as_view({"get": "list", "post": "create"})),


    path("price-models/<int:price_model_pk>/daily-prices/<int:pk>/",
         DailyPriceModelViewSet.as_view({"get": "retrieve",
                                         'put': 'update',
                                         'patch': 'partial_update',
                                         'delete': 'destroy',
                                         })),

]


urlpatterns = router.urls + daily_prices_urls
