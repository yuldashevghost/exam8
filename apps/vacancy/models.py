from django.db import models


# Create your models here.
class Vacancy(models.Model):
    title = models.CharField(max_length=125)
    description = models.TextField()
    salary_from = models.CharField(max_length=125)
    salary_to = models.CharField(max_length=125)
    salary = models.IntegerField()

    def __str__(self):
        return self.title
