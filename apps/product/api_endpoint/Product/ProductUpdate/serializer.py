from rest_framework import serializers

from apps.product.models import Product


class ProductUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
