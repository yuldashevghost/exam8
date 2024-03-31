from rest_framework import serializers

from apps.sport.models import Sport


class SportDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Sport
        fields = '__all__'