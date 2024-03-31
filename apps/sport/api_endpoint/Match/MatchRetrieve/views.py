from rest_framework.generics import RetrieveAPIView

from apps.sport.api_endpoint.Match.MatchRetrieve.serializer import MatchRetrieveSerializer
from apps.sport.models import Match


class MatchRetrieveAPIView(RetrieveAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchRetrieveSerializer

__all__ = ['MatchRetrieveAPIView']