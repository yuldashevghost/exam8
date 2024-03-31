from rest_framework.generics import UpdateAPIView

from apps.sport.api_endpoint.Chempionship.ChempionshipUpdate.serializer import ChempionshipUpdateSerializer
from apps.sport.models import Chempionship


class ChempionshipUpdateAPIView(UpdateAPIView):
    queryset = Chempionship.objects.all()
    serializer_class = ChempionshipUpdateSerializer

__all__ = ['ChempionshipUpdateAPIView']