from rest_framework.generics import ListAPIView

from apps.sport.api_endpoint.Sport.SportList.serializer import SportListSerializer
from apps.sport.models import Sport


class SportListAPIView(ListAPIView):
    queryset = Sport.objects.all()
    serializer_class = SportListSerializer

__all__ = ['SportListAPIView']