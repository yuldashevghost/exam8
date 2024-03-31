from rest_framework import serializers

from apps.sport.models import Match


class MatchDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'
