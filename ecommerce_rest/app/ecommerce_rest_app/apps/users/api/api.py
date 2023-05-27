from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view
from apps.users.models import User
from apps.users.api.serializers import UserSerializer
from django.shortcuts import get_object_or_404

@api_view(['GET', 'POST'])
def UserAPIViewDecorator(request):
    if request.method == 'GET':
        u = User.objects.all()
        serializer = UserSerializer(u, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def User_Dtl_API_View(request, id):
    #u = User.objects.filter(id=id).first()
    u = get_object_or_404(User, id=id)

    if request.method == 'GET':
        serializer = UserSerializer(u)
        return Response({'msg':'usuario encontrado','data': serializer.data}, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = UserSerializer(u, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        u.delete()
        return Response('Eliminado', status=status.HTTP_204_NO_CONTENT)

class UserAPIView(APIView):
    def get(self, request):
        u = User.objects.all()

        serializer = UserSerializer(u, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)