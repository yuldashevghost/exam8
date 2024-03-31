from rest_framework import serializers

from apps.vacancy.models import Vacancy


class VacancyRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = "__all__"
