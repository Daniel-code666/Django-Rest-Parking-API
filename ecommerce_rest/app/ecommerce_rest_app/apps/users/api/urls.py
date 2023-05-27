from django.urls import path
from apps.users.api.api import *

urlpatterns = [
    path('user/', UserAPIView.as_view(), name='users_api'),
    path('userwdecorator/', UserAPIViewDecorator, name='users_api_decorator'),
    path('userdtlview/<int:id>', User_Dtl_API_View, name='user_dtl_view'),
]