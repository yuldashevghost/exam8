from rest_framework import serializers

from apps.product.api_endpoint.Product.ProductShiferList.aes import encrypt, decrypt
from apps.product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    price = serializers.CharField()
    marja = serializers.CharField()

    class Meta:
        model = Product
        fields = ["id", "price", "marja", "package_code"]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["price"] = encrypt(str(instance.price).zfill(16))
        data["marja"] = encrypt(str(instance.margin).zfill(16))
        return data

    def to_internal_value(self, data):
        data["price"] = decrypt(data["price"]).lstrip("0")
        data["marja"] = decrypt(data["marja"]).lstrip("0")
        return super().to_internal_value(data)
