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
    path('change-password/', ChangePasswordApiView.as_view(), name='change_password'),
    path('profile/', ProfileGetApiView.as_view(), name='profile-get'),
    path('profile/<int:pk>/', ProfileApiView.as_view(), name='profile-list'),
    path('address/<int:pk>/', AddressApiView.as_view(), name='delete_address'),
]
