from rest_framework.generics import RetrieveAPIView

from apps.sport.api_endpoint.Sport.SportRetrieve.serializer import SportRetrieveSerializer
from apps.sport.models import Sport


class SportRetrieveAPIView(RetrieveAPIView):
    queryset = Sport.objects.all()
    serializer_class = SportRetrieveSerializer

__all__ = ['SportRetrieveAPIView']