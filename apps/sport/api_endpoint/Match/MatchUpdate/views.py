from rest_framework import viewsets
from rest_framework.generics import UpdateAPIView

from apps.sport.api_endpoint.Match.MatchUpdate.serializer import MatchUpdateSerializer
from apps.sport.models import Match


class MatchUpdateAPIView(UpdateAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchUpdateSerializer


__all__ = ["MatchUpdateAPIView"]
