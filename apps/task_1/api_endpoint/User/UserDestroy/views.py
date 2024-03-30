from rest_framework.generics import DestroyAPIView

from apps.task_1.api_endpoint.User.UserDestroy.Serializer import UserDestroySerializer
from apps.task_1.models import User


class UserDestroyAPIView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDestroySerializer

__all__ = ['UserDestroyAPIView']

