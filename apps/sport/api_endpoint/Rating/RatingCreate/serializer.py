from rest_framework import serializers

from apps.sport.models import Rating


class RatingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = "__all__"
