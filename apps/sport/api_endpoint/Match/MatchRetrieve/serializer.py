from rest_framework import serializers

from apps.sport.models import Match


class MatchRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'