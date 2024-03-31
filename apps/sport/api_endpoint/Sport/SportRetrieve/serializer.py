from rest_framework import serializers

from apps.sport.models import Sport


class SportRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sport
        fields = "__all__"
