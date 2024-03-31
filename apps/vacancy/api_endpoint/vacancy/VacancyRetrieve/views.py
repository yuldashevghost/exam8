from rest_framework.generics import RetrieveAPIView

from apps.vacancy.api_endpoint.vacancy.VacancyRetrieve.Serializer import (
    VacancyRetrieveSerializer,
)
from apps.vacancy.models import Vacancy


class VacancyRetrieveAPIView(RetrieveAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancyRetrieveSerializer


__all__ = ["VacancyRetrieveAPIView"]
