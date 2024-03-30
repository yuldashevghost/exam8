from rest_framework.generics import UpdateAPIView

from apps.user.api_endpoint.User.UserUpdate.serializer import UserUpdateSerializer
from apps.user.models import User


class UserUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer


__all__ = ["UserUpdateView"]
