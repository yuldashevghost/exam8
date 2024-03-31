from rest_framework import serializers

from apps.sport.models import Rating


class RatingRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = "__all__"
