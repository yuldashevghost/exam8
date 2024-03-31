from rest_framework.views import APIView

from apps.vacancy.models import Vacancy
from .serializer import VacancySerializer


class VacancyAPIView(APIView):

    serializer_class = VacancySerializer

    def get_queryset(self):
        queryset = Vacancy.objects.all()
        salary_from = self.request.query_params.get("salary_from")
        salary_to = self.request.query_params.get("salary_to")
        salary = self.request.query_params.get("salary")

        if salary_from is not None:
            queryset = queryset.filter(salary__gte=salary_from)
        if salary_to is not None:
            queryset = queryset.filter(salary__lte=salary_to)
        if salary is not None:
            queryset = queryset.filter(salary=salary)
        return queryset


__all__ = ["VacancyAPIView"]
