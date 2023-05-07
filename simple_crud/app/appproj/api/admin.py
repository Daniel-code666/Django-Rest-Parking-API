from django.contrib import admin
from .models import Parking, Car, ApiTask

myModels = [Parking, Car]

# Register your models here.
admin.site.register(myModels)