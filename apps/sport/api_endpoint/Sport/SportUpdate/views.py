from rest_framework.generics import UpdateAPIView

from apps.sport.api_endpoint.Sport.SportUpdate.serializer import SportUpdateSerializer
from apps.sport.models import Sport


class SportUpdateAPIView(UpdateAPIView):
    queryset = Sport.objects.all()
    serializer_class = SportUpdateSerializer

__all__ = ['SportUpdateAPIView']