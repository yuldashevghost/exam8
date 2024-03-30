from rest_framework import generics

from apps.task_1.api_endpoint.User.UserCreate.serializer import UserCreateSerializer
from apps.task_1.models import User


class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

__all__ = ['UserCreateAPIView']