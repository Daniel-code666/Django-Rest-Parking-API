from rest_framework import generics, viewsets
from rest_framework.response import Response
from apps.base.api import GeneralListApiView
from apps.products.api.serializers.general_serializers import *
from apps.products.models import *

# views with viewsets
class MeasureUnitListViewSetAPIView(viewsets.GenericViewSet):
    model = MeasureUnit
    serializer_class = MeasureUnitSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state=True)

    def list(self, request):
        data = self.get_queryset()
        data = self.get_serializer(data, many=True)
        return Response(data.data)

class CategoryProductViewSetListAPIView(viewsets.ModelViewSet):
    serializer_class = CategoryProductSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state=True)

    def list(self, request):
        data = self.get_queryset()
        data = self.get_serializer(data, many=True)
        return Response(data.data)

class IndicatorListViewSetAPIView(viewsets.ModelViewSet):
    serializer_class = IndicatorSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state=True)


# views with common general view
class MeasureUnitListAPIView(GeneralListApiView):
    serializer_class = MeasureUnitSerializer

class CategoryProductListAPIView(GeneralListApiView):
    serializer_class = CategoryProductSerializer

class IndicatorListAPIView(GeneralListApiView):
    serializer_class = IndicatorSerializer
