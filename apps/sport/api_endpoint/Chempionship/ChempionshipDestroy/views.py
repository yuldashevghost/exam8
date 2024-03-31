from rest_framework.generics import DestroyAPIView

from apps.sport.api_endpoint.Chempionship.ChempionshipDestroy.serializer import (
    ChempionshipDestroySerializer,
)
from apps.sport.models import Chempionship


class ChempionshipDestroyAPIView(DestroyAPIView):
    queryset = Chempionship.objects.all()
    serializer_class = ChempionshipDestroySerializer


__all__ = ["ChempionshipDestroyAPIView"]
