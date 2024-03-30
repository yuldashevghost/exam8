from rest_framework import generics

from apps.task_1.api_endpoint.User.UserList.serializer import UserListSerializer
from apps.task_1.models import User


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer

__all__ = ['UserListView']