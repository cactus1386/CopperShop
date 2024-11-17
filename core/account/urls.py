from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)


app_name = "api-v1"

urlpatterns = [
    # Auth
    path(
        "token/logout/",
        views.CustomDiscardAuthToken.as_view(),
        name="token-logout",
    ),
    path(
        "jwt/create/",
        views.CustomTokenObtainPairView.as_view(),
        name="JWT-token-create",
    ),
    path(
        "jwt/refresh/", TokenRefreshView.as_view(), name="JWT-token-refresh"
    ),
    path("jwt/verify/", TokenVerifyView.as_view(), name="JWT-token-verify"),
    path(
        "password-change/",
        views.ChangePasswordApiView.as_view(),
        name="change-password",
    ),
    # Profile
    path("profile/<int:pk>", views.ProfileApiView.as_view(), name="profile"),
    path("profile/", views.GetProfileApiView.as_view(), name="get-profile"),

    # Address
    path("address/<int:pk>", views.AddressApiView.as_view(), name="address"),
]
