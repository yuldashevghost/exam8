from rest_framework.generics import UpdateAPIView

from apps.product.api_endpoint.Product.ProductUpdate.serializer import (
    ProductUpdateSerializer,
)
from apps.product.models import Product


class ProductUpdateAPIView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductUpdateSerializer


__all__ = ["ProductUpdateAPIView"]
