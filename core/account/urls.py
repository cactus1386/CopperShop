from django.urls import path, include
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)


app_name = "api-v1"


urlpatterns = [
    path(
        "jwt/create/",
        CustomTokenObtainPairView.as_view(),
        name="JWT-token-create",
    ),
    path(
        "jwt/refresh/", TokenRefreshView.as_view(), name="JWT-token-refresh"
    ),
    path("jwt/verify/", TokenVerifyView.as_view(), name="JWT-token-verify"),
    path('register/', RegistrationApiView.as_view(), name="register"),
    path('change-password/', ChangePasswordApiView.as_view(), name='change_password'),
    path('profile/<int:pk>/', ProfileApiView.as_view(), name='profile'),
    path('address/', AddressApiView.as_view(), name='address'),
    path('address/<int:pk>/', AddressDetailApiView.as_view(), name='address-detail'),
]
