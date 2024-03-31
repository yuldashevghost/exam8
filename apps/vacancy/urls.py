from django.urls import path

from apps.vacancy.api_endpoint.vacancy import (
    VacancyListAPIView,
    VacancyCreateAPIView,
    VacancyUpdateAPIView,
    VacancyDeleteAPIView,
)
from apps.vacancy.api_endpoint.vacancy.VacancyTransmission.views import VacancyAPIView

urlpatterns = [
    path("vacancie/", VacancyAPIView.as_view()),
    path("vacancies/", VacancyListAPIView.as_view()),
    path("vacancies/create", VacancyCreateAPIView.as_view()),
    path("vacancies/<pk>/update", VacancyUpdateAPIView.as_view()),
    path("vacancies/<pk>/delete", VacancyDeleteAPIView.as_view()),
    path("vacancies/<pk>/retrieve", VacancyAPIView.as_view()),
]
