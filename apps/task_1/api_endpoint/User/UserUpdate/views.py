from rest_framework.generics import UpdateAPIView

from apps.task_1.api_endpoint.User.UserUpdate.serializer import UserUpdateSerializer
from apps.task_1.models import User


class UserUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer


__all__ = ["UserUpdateView"]
