from rest_framework.generics import RetrieveAPIView

from apps.task_1.api_endpoint.User.UserRetrieve.serializer import UserRetrieveSerializer
from apps.task_1.models import User


class UserRetrieveAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserRetrieveSerializer


__all__ = ["UserRetrieveAPIView"]
