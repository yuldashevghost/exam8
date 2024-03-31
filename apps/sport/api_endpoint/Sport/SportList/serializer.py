from rest_framework import serializers

from apps.sport.models import Sport


class SportListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sport
        fields = '__all__'