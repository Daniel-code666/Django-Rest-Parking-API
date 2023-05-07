from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from django.db.models import OuterRef, Subquery
from .models import Parking, Car
from .serializers import CarSerializer, ParkingSerializer, ParkingPostSerializer
from rest_framework_swagger.views import get_swagger_view
from rest_framework_swagger import renderers
from rest_framework.permissions import AllowAny
from rest_framework.schemas import SchemaGenerator
from django.db import connection
from datetime import datetime
from django.shortcuts import get_object_or_404

# Create your views here.

class GetCars_APIView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        cars = Car.objects.all()
        return Response(CarSerializer(cars, many=True).data)

class Postcar_APIView(APIView):
    def post(self, request, *args, **kwargs):

        car = Car.objects.filter(car_idnum = request.data.get("car_idnum"))

        if request.data.get("car_idnum") == None:
            return Response(request.data, status=status.HTTP_400_BAD_REQUEST)

        if car.exists():
            return Response("El número de placa ya existe", status=status.HTTP_400_BAD_REQUEST)

        serializer = CarSerializer(data=request.data)

        car_parking_id = request.data.get("car_parking_id")

        if serializer.is_valid():
            parking = Parking.objects.only("parking_tot_cars").filter(parking_id = car_parking_id)

            for i in parking:
                curr_cars = i.parking_tot_cars

            curr_cars = curr_cars + 1

            serializer.save()

            with connection.cursor() as cursor:
                cursor.execute("UPDATE public.api_parking SET parking_tot_cars = %s WHERE parking_id = %s;", [curr_cars, car_parking_id])

            return Response("Vehículo creado", status=status.HTTP_200_OK)

class UpdateCar_APIView(APIView):
    def patch(self, request, car_id):
        car = Car.objects.filter(car_idnum = request.data.get("car_idnum")) 

        if car.exists():
            return Response("El número de placa ya existe", status=status.HTTP_400_BAD_REQUEST)

        car = Car.objects.filter(car_id = car_id)

        if not car.exists():
            return Response("El vehículo no existe", status=status.HTTP_400_BAD_REQUEST)

        car = Car.objects.get(car_id = car_id)

        car.car_brand = request.data.get("car_brand", car.car_brand)
        car.car_model = request.data.get("car_model", car.car_model)
        car.car_idnum = request.data.get("car_idnum", car.car_idnum)
        car.car_is_parked = request.data.get("car_is_parked", car.car_is_parked)
        car.car_parking_id = request.data.get("car_parking_id", car.car_parking_id)
        car.car_parked_at = request.data.get("car_parked_at", datetime.now())
        car.car_updated_at = request.data.get("car_updated_at", datetime.now())

        car.save()

        serializer = CarSerializer(car)
        return Response(serializer.data)

class DeleteCar_APIView(APIView):
    def delete(self, request, car_id = 0, car_idnum = ''):
        if car_id != 0:
            car = Car.objects.get(car_id=car_id)

            if car == None:
                return Response("No se ha encontrado el vehículo", status=status.HTTP_400_BAD_REQUEST)

            car.delete()
            return Response("Vehículo eliminado por id", status=status.HTTP_204_DELETED)
        elif car_idnum != '':
            car = Car.objects.get(car_idnum=car_idnum)

            if car == None:
                return Response("No se ha encontrado el vehículo", status=status.HTTP_400_BAD_REQUEST)

            car.delete()
            return Response("Vehículo eliminado por número de placa", status=status.HTTP_204_NO_CONTENT)
        else:
            return Response("No se enviaron parámetros para la petición", status=status.HTTP_400_BAD_REQUEST)

class GetParkingsWCars_APIView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        parkings = Parking.objects.all()

        return Response(ParkingSerializer(parkings, many=True).data)

class CreateParkings_APIView(APIView):
    def post(self, request):

        if request.data.get("parking_name") == '':
            return Response("No hay nombre de parqueadero", status=status.HTTP_400_BAD_REQUEST)

        parking = Parking.objects.filter(parking_name=request.data.get("parking_name"))

        if parking.exists():
            return Response("El parqueadero ya existe", status=status.HTTP_400_BAD_REQUEST)

        serialize = ParkingPostSerializer(data=request.data)

        if serialize.is_valid():
            serialize.save()
            return Response("Parqueadero creado", status=status.HTTP_200_OK)

class UpdateParking_APIView(APIView):
    def patch(self, request, parking_id):
        parking = get_object_or_404(Parking, parking_id=parking_id)

        if request.data == None:
            return Response("No hay datos para hacer la actualización", status=status.HTTP_400_BAD_REQUEST)

        if request.data.get('parking_name') != None:
            req_parking_name = request.data.get('parking_name')

            if parking.parking_name != req_parking_name:
                if Parking.objects.filter(parking_name=req_parking_name).exists():
                    return Response("El nombre del parqueadero ya existe", status=status.HTTP_400_BAD_REQUEST)
                parking.parking_name = req_parking_name

        parking.parking_tot_cars = request.data.get('parking_tot_cars', parking.parking_tot_cars)
        parking.parking_created_at = request.data.get('parking_created_at', parking.parking_created_at)
        parking.parking_updated_at = request.data.get('parking_updated_at', parking.parking_updated_at)

        parking.save()

        serializer = ParkingSerializer(parking)

        return Response(serializer.data, status=status.HTTP_200_OK)

class DeleteParking_APIView(APIView):
    def delete(self, request, parking_id):
        parking = get_object_or_404(Parking, parking_id=parking_id)

        parking.delete()
        return Response("Parqueadero eliminado", status=status.HTTP_204_NO_CONTENT)

