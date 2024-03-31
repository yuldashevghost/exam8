from rest_framework.generics import DestroyAPIView

from apps.sport.api_endpoint.Sport.SportDestroy.serializer import SportDestroySerializer
from apps.sport.models import Sport


class SportDestroyAPIView(DestroyAPIView):
    queryset = Sport.objects.all()
    serializer_class = SportDestroySerializer

__all__ = ['SportDestroyAPIView']