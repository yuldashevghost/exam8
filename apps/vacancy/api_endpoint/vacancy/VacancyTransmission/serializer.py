from rest_framework import serializers

from apps.vacancy.models import Vacancy


class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ["id", "title", "description", "salary_from", "salary_to", "salary"]
