from rest_framework.generics import CreateAPIView

from apps.sport.api_endpoint.Sport.SportCreate.serializer import SportCreateSerializer
from apps.sport.models import Sport


class SportCreateAPIView(CreateAPIView):
    queryset = Sport.objects.all()
    serializer_class = SportCreateSerializer

__all__ = ['SportCreateAPIView']