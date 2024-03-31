from rest_framework import serializers

from apps.sport.models import Team


class TeamDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

