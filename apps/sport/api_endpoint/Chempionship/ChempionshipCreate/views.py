from rest_framework.generics import CreateAPIView

from apps.sport.api_endpoint.Chempionship.ChempionshipCreate.serializer import (
    ChempionshipCreateSerializer,
)
from apps.sport.models import Chempionship


class ChempionshipCreateAPIView(CreateAPIView):
    queryset = Chempionship.objects.all()
    serializer_class = ChempionshipCreateSerializer


__all__ = ["ChempionshipCreateAPIView"]
