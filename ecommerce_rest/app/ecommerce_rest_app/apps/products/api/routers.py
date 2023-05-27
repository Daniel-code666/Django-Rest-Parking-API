from rest_framework.routers import DefaultRouter
from apps.products.api.views.product_views import ProductViewSet
from apps.products.api.views.general_views import *

router = DefaultRouter()

router.register(r'products', ProductViewSet)
router.register(r'prodsoverwrite', ProductViewSet, basename='prodsovwr')
router.register(r'measureviewset', MeasureUnitListViewSetAPIView, basename='measureviewset')
router.register(r'categoryviewset', CategoryProductViewSetListAPIView, basename='categoryviewset')
router.register(r'indicatorviewset', IndicatorListViewSetAPIView, basename='indicatorviewset')

urlpatterns = router.urls
