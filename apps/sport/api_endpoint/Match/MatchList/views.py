from rest_framework.generics import ListAPIView

from apps.sport.api_endpoint.Match.MatchList.serializer import MatchListSerializer
from apps.sport.models import Match


class MatchListAPIView(ListAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchListSerializer


__all__ = ["MatchListAPIView"]
