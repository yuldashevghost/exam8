from django.contrib import admin

from apps.vacancy.models import Vacancy


# Register your models here.
@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    pass
