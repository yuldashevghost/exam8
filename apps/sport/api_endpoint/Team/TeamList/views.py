from rest_framework.generics import ListAPIView

from apps.sport.api_endpoint.Team.TeamList.serializer import TeamListSerializer
from apps.sport.models import Team


class TeamListAPIView(ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamListSerializer


__all__ = ["TeamListAPIView"]
