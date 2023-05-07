from rest_framework import serializers
from .models import Parking, Car

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'

class ParkingPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parking
        fields = '__all__'

class ParkingSerializer(serializers.ModelSerializer):
    cars =  CarSerializer(many=True)
    class Meta:
        model = Parking
        fields = ['parking_id', 'parking_name', 'parking_tot_cars', 'parking_created_at', 'parking_updated_at', 'cars']

