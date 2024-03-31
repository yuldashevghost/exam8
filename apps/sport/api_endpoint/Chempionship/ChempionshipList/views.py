from rest_framework.generics import ListAPIView

from apps.sport.api_endpoint.Chempionship.ChempionshipList.serializer import ChempionshipListSerializer
from apps.sport.models import Chempionship


class ChempionshipListAPIView(ListAPIView):
    queryset = Chempionship.objects.all()
    serializer_class = ChempionshipListSerializer

__all__ = ['ChempionshipListAPIView']