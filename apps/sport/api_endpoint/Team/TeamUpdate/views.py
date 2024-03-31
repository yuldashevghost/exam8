from rest_framework.generics import UpdateAPIView

from apps.sport.api_endpoint.Team.TeamUpdate.serializer import TeamUpdateSerializer
from apps.sport.models import Team


class TeamUpdateAPIView(UpdateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamUpdateSerializer


__all__ = ["TeamUpdateAPIView"]
