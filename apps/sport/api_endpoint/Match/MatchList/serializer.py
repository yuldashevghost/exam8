from django.db.models import Model
from rest_framework import serializers


class MatchListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = "__all__"
