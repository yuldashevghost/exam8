from rest_framework import serializers

from apps.sport.models import Rating


class RatingDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'