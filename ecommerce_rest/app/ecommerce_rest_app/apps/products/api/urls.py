from django.urls import path
from apps.users.api.api import *
from apps.products.api.views.general_views import *
from apps.products.api.views.product_views import *

urlpatterns = [
    path('measureunit/', MeasureUnitListAPIView.as_view(), name='measure_unit'),
    path('categoryprod/', CategoryProductListAPIView.as_view(), name='category_prod'),
    path('indicator/', IndicatorListAPIView.as_view(), name='indicator'),
    path('product/', ProductListAPIView.as_view(), name='product'),
    path('listcreateproduct/', ProductListCreateAPIView.as_view(), name='list_created_prod'),
    path('createproduct/', ProductCreateAPIView.as_view(), name='product_create'),
    path('retupdtdelprod/<int:pk>', ProductRetrieveUpdateDestroyAPIView.as_view(), name="product_retirve_update"),
    path('retrieveproduct/<int:pk>', ProductRetrieveAPIView.as_view(), name='product_retrieve'),
    path('deleteproduct/<int:pk>', ProductDestroyAPIView.as_view(), name='product_delete'),
    path('updateproduct/<int:pk>', ProductUpdateAPIView.as_view(), name="product_update")
]