from django.contrib.auth.models import AbstractUser
from django.db import models
from django_softdelete.models import SoftDeleteModel


class User(SoftDeleteModel, AbstractUser):
    email = models.EmailField(unique=True)