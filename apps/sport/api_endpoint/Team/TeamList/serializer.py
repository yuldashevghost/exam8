from rest_framework import serializers

from apps.sport.models import Team


class TeamListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = "__all__"
