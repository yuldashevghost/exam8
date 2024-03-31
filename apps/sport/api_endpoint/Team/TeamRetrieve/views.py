from rest_framework.generics import RetrieveAPIView

from apps.sport.api_endpoint.Team.TeamRetrieve.serializer import TeamRetrieveSerializer
from apps.sport.models import Team


class TeamRetrieveAPIView(RetrieveAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamRetrieveSerializer