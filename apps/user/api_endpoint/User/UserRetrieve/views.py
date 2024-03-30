from rest_framework.generics import RetrieveAPIView

from apps.user.api_endpoint.User.UserRetrieve.serializer import UserRetrieveSerializer
from apps.user.models import User


class UserRetrieveAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserRetrieveSerializer


__all__ = ["UserRetrieveAPIView"]
