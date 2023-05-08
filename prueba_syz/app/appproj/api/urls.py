from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('drivers/', views.GetCondutores_APIView.as_view()),
    path('createdriver/', views.PostConductor_APIView.as_view()),
    path('deletedriver/<int:id>', views.DeleteConductor_APIView.as_view()),
    path('updatedriver/<int:id>', views.UpdateConductor_APIView.as_view())
]