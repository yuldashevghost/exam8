from rest_framework.generics import CreateAPIView

from apps.product.api_endpoint.Product.ProductCreate.serializer import (
    ProductCreateSerializer,
)
from apps.product.models import Product


class ProductCreateAPIView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer


__all__ = ["ProductCreateAPIView"]
