from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('cars/', views.GetCars_APIView.as_view()),
    path('parkings/', views.GetParkingsWCars_APIView.as_view()),
    path('createcar/', views.Postcar_APIView.as_view()),
    path('updatecar/<int:car_id>', views.UpdateCar_APIView.as_view()),
    path('deletecar/<int:car_id>/<str:car_idnum>', views.DeleteCar_APIView.as_view()),
    path('createparking/', views.CreateParkings_APIView.as_view()),
    path('updateparking/<int:parking_id>', views.UpdateParking_APIView.as_view()),
    path('deleteparking/<int:parking_id>', views.DeleteParking_APIView.as_view()),
]