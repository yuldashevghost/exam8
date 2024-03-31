from django.db import models


# Create your models here.
class Product(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    marja = models.DecimalField(max_digits=10, decimal_places=2)
    package_code = models.CharField(max_length=125)

    def __str__(self):
        return self.package_code
