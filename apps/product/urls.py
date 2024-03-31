from django.urls import path

from apps.product.api_endpoint.Product import (
    ProductListAPIView,
    ProductCreateAPIView,
    ProductUpdateAPIView,
    ProductDestroyAPIView,
    ProductRetrieveAPIView,
)

urlpatterns = [
    path("product/", ProductListAPIView.as_view()),
    path("product/create/", ProductCreateAPIView.as_view()),
    path("product/<pk>/update/", ProductUpdateAPIView.as_view()),
    path("product/<pk>/destroy/", ProductDestroyAPIView.as_view()),
    path("product/<pk>/retrieve/", ProductRetrieveAPIView.as_view()),
]
