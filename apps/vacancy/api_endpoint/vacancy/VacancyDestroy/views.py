from rest_framework.generics import DestroyAPIView

from apps.vacancy.api_endpoint.vacancy.VacancyDestroy.serializer import (
    VacancyDestroySerializer,
)
from apps.vacancy.models import Vacancy


class VacancyDeleteAPIView(DestroyAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancyDestroySerializer


__all__ = ["VacancyDeleteAPIView"]
