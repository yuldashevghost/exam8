from rest_framework import generics
from rest_framework.response import Response
from apps.product.models import Product


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serialized_data = []

        for produc in queryset:
            serialized_product = produc.serialize()
            serialized_data.append(serialized_product)

        return Response(serialized_data)


__all__ = ["ProductListAPIView"]
