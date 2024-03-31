from rest_framework.generics import UpdateAPIView

from apps.vacancy.api_endpoint.vacancy.VacanctUpdate.serializer import (
    VacancyUpdateSerializer,
)
from apps.vacancy.models import Vacancy


class VacancyUpdateAPIView(UpdateAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancyUpdateSerializer


__all__ = ["VacancyUpdateAPIView"]
