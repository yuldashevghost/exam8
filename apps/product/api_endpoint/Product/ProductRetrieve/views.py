from rest_framework.generics import RetrieveAPIView

from apps.product.api_endpoint.Product.ProductRetrieve.serializer import (
    ProductRetrieveSerializer,
)
from apps.product.models import Product


class ProductRetrieveAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductRetrieveSerializer


__all__ = ["ProductRetrieveAPIView"]
