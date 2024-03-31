from rest_framework.generics import DestroyAPIView

from apps.product.api_endpoint.Product.ProductDestroy.serializer import (
    ProductDestroySerializer,
)
from apps.product.models import Product


class ProductDestroyAPIView(DestroyAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductDestroySerializer


__all__ = ["ProductDestroyAPIView"]
