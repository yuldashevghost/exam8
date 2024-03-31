from rest_framework import serializers

from apps.sport.models import Rating


class RatingUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = "__all__"
