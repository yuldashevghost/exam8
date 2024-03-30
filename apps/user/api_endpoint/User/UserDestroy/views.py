from rest_framework.generics import DestroyAPIView

from apps.user.api_endpoint.User.UserDestroy.Serializer import UserDestroySerializer
from apps.user.models import User


class UserDestroyAPIView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDestroySerializer


__all__ = ["UserDestroyAPIView"]
