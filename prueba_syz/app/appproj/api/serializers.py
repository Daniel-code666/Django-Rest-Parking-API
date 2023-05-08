from rest_framework import serializers
from .models import Conductores

class ConductorSerializer(serializers.ModelSerializer):
    class Meta:
        model= Conductores
        fields = '__all__'