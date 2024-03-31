from rest_framework import serializers

from apps.sport.models import Chempionship


class ChempionshipUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chempionship
        fields = '__all__'