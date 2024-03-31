from rest_framework import serializers
from rest_framework.generics import CreateAPIView

from apps.vacancy.models import Vacancy


class VacancyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = "__all__"
