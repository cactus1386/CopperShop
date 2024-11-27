from django.shortcuts import get_object_or_404
from rest_framework import generics
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from account.models import Profile, User, Address
from rest_framework_simplejwt.views import TokenObtainPairView


class ObtainAuthTokenView(ObtainAuthToken):
    serializer_class = CustomAuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        return Response(
            {
                "token": token.key,
                "user_id": user.pk,
                "phone": user.phone,
            }
        )


class CustomDiscardAuthToken(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ChangePasswordApiView(generics.GenericAPIView):
    model = User
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer

    def get_object(self):
        obj = self.request.user
        return obj

    def put(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            if not self.object.check_password(
                serializer.data.get("old_password")
            ):
                return Response(
                    {"old_password": ["Wrong Password."]},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return Response(
                {"success": "Password updated successfully."},
                status=status.HTTP_200_OK,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileApiView(generics.CreateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)


class GetProfileApiView(generics.ListAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class AddressApiView(generics.ListCreateAPIView):
    serializer_class = AddressSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Address.objects.none()
        profile = Profile.objects.get(user=self.request.user)
        return Address.objects.filter(profile=profile)

    def delete(self, request, *args, **kwargs):
        profile = Profile.objects.get(user=request.user)
        try:
            address = Address.objects.get(profile=profile, id=kwargs.get("pk"))
            address.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Address.DoesNotExist:
            return Response({"error": "Address not found."}, status=status.HTTP_404_NOT_FOUND)
