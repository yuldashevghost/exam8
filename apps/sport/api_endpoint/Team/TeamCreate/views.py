from rest_framework.generics import CreateAPIView

from apps.sport.api_endpoint.Team.TeamCreate.serializer import TeamCreateSerializer
from apps.sport.models import Team


class TeamCreateAPIView(CreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamCreateSerializer

__all__ = ['TeamCreateAPIView']