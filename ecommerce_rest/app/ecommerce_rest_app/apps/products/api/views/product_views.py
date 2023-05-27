from django.shortcuts import get_object_or_404
from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from apps.base.api import GeneralListApiView
from apps.products.api.serializers.product_serializer import *
from apps.products.api.serializers.general_serializers import * 

# all methods on same view, but overwriting the methods
class ProductViewSetOvrwMethods(viewsets.ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state=True)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'producto creado', 'data':serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        p = get_object_or_404(Product, id=pk)

        prod_ser = self.serializer_class(p)
        return Response({'msg':'actualizado', 'data':prod_ser.data}, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        p = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(p)
        p.state = False
        p.save()
        return Response({'msg':'eliminado', 'data':serializer.data}, status=status.HTTP_200_OK)

# all methods on the same view
class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = ProductSerializer.Meta.model.objects.filter(state=True)

# product list
class ProductListAPIView(GeneralListApiView):
    serializer_class = ProductSerializer

# list of products with create form
class ProductListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer

    queryset = ProductSerializer.Meta.model.objects.filter(state=True)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'producto creado', 'data':serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# create form for the product
class ProductCreateAPIView(generics.CreateAPIView):
    serializer_class = ProductSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'producto creado', 'data':serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# update, recover and delete product by id on same view
class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer

    def get(self, request, pk=None):
        p = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(p)
        return Response({'msg':'objeto encontrado!', 'data':serializer.data}, status=status.HTTP_200_OK)

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state=True)

    def patch(self, request, pk=None):
        p = get_object_or_404(Product, id=pk)

        prod_ser = self.serializer_class(p)
        return Response({'msg':'actualizado', 'data':prod_ser.data}, status=status.HTTP_200_OK)

    def delete(self, request, pk=None):
        p = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(p)
        p.state = False
        p.save()
        return Response({'msg':'eliminado', 'data':serializer.data}, status=status.HTTP_200_OK)

# get product by id
class ProductRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ProductSerializer
    
    # def get_queryset(self):
    #     return self.get_serializer().Meta.model.objects.filter(state=True)
    
    def get(self, request, pk=None):
        p = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(p)
        return Response({'msg':'objeto encontrado!', 'data':serializer.data}, status=status.HTTP_200_OK)

# delete product by id
class ProductDestroyAPIView(generics.DestroyAPIView):
    serializer_class = ProductSerializer

    def delete(self, request, pk=None):
        p = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(p)
        p.state = False
        p.save()
        return Response({'msg':'eliminado', 'data':serializer.data}, status=status.HTTP_200_OK)

#update product
class ProductUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state=True)

    def patch(self, request, pk=None):
        p = get_object_or_404(Product, id=pk)
        
        prod_ser = self.serializer_class(p)

        return Response({'msg':'actualizado', 'data':prod_ser.data}, status=status.HTTP_200_OK)

