from rest_framework.generics import CreateAPIView

from apps.sport.api_endpoint.Match.MatchCreate.Serializer import MatchCreateSerializer
from apps.sport.models import Match


class MatchCreateAPIView(CreateAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchCreateSerializer


__all__ = ["MatchCreateAPIView"]
