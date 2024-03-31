from rest_framework.generics import DestroyAPIView

from apps.sport.api_endpoint.Team.TeamDestroy.serializer import TeamDestroySerializer
from apps.sport.models import Team


class TeamDestroyAPIView(DestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamDestroySerializer


__all__ = ["TeamDestroyAPIView"]
