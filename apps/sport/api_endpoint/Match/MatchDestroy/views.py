from rest_framework.generics import DestroyAPIView

from apps.sport.api_endpoint.Match.MatchDestroy.serializer import MatchDestroySerializer
from apps.sport.models import Match


class MatchDestroyAPIVIew(DestroyAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchDestroySerializer

__all__ = ['MatchDestroyAPIVIew']