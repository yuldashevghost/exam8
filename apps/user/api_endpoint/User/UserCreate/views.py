from rest_framework import generics

from apps.user.api_endpoint.User.UserCreate.serializer import UserCreateSerializer
from apps.user.models import User


class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


__all__ = ["UserCreateAPIView"]
