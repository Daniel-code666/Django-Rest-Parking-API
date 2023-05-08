from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status, generics
from rest_framework.response import Response
from .serializers import ConductorSerializer
from .models import Conductores
from django.shortcuts import get_object_or_404


# Create your views here.
class GetCondutores_APIView(APIView):
    def get(self, request, *args, **kwargs):
        c = Conductores.objects.all()
        cSerializer = ConductorSerializer(c, many=True)
        return Response(cSerializer.data, status=status.HTTP_200_OK)

class PostConductor_APIView(APIView):
    def post(self, request):
        cSerialize = ConductorSerializer(data=request.data)
        if cSerialize.is_valid():
            cSerialize.save()
            return Response("Conductor creado", status=status.HTTP_201_CREATED)

class UpdateConductor_APIView(APIView):
    def patch(self, request, id):
        conductor = get_object_or_404(Conductores, id=id)
        
        conductor.nombre = request.data.get('nombre', conductor.nombre)
        conductor.apellido = request.data.get('apellido', conductor.apellido)
        conductor.fecha_nacimiento = request.data.get('fecha_nacimiento', conductor.fecha_nacimiento)
        conductor.direccion = request.data.get('direccion', conductor.direccion)
        conductor.codigo_postal = request.data.get('codigo_postal', conductor.codigo_postal)
        conductor.licencia_conducir = request.data.get('licencia_conducir', conductor.licencia_conducir)
        conductor.fecha_vencimiento_licencia = request.data.get('fecha_vencimiento_licencia', conductor.fecha_vencimiento_licencia)
        conductor.created_at = request.data.get('created_at', conductor.created_at)
        conductor.updated_at = request.data.get('update_at', conductor.updated_at)

        conductor.save()

        serializer = ConductorSerializer(conductor)
        return Response(serializer.data, status=status.HTTP_200_OK)

class DeleteConductor_APIView(APIView):
    def delete(self, request, id):
        conductor = get_object_or_404(Conductores, id=id)
        conductor.delete()

        return Response("Eliminado", status=status.HTTP_204_NO_CONTENT)

