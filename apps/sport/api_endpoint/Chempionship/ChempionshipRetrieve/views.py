from rest_framework.generics import RetrieveAPIView

from apps.sport.api_endpoint.Chempionship.ChempionshipRetrieve.serializer import ChempionshipRetrieveSerializer
from apps.sport.models import Chempionship


class ChempionshipRetrieveAPIView(RetrieveAPIView):
    queryset = Chempionship.objects.all()
    serializer_class = ChempionshipRetrieveSerializer

__all__ = ['ChempionshipRetrieveAPIView']