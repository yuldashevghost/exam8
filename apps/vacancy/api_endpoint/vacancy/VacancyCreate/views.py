from rest_framework.generics import CreateAPIView

from apps.vacancy.api_endpoint.vacancy.VacancyCreate.serializer import (
    VacancyCreateSerializer,
)
from apps.vacancy.models import Vacancy


class VacancyCreateAPIView(CreateAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancyCreateSerializer


__all__ = ["VacancyCreateAPIView"]
