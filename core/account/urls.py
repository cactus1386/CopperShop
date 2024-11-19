from django.urls import path, include
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)


app_name = "api-v1"


urlpatterns = [
    path('login/', ObtainAuthTokenView.as_view(), name='login'),
    path('logout/', CustomDiscardAuthToken.as_view(), name='logout'),
    path('change-password/', ChangePasswordApiView.as_view(), name='change_password'),
    path('profile/', ProfileApiView.as_view(), name='profile'),
    path('profile/list/', GetProfileApiView.as_view(), name='get_profile'),
    path('address/', AddressApiView.as_view(), name='address'),
    path('address/<int:pk>/', AddressApiView.as_view(), name='delete_address'),
]
