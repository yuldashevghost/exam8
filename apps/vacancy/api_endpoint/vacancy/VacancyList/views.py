from rest_framework.generics import ListAPIView

from apps.vacancy.api_endpoint.vacancy.VacancyList.serializer import (
    VacancyListSerializer,
)
from apps.vacancy.models import Vacancy


class VacancyListAPIView(ListAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancyListSerializer


__all__ = ["VacancyListAPIView"]
