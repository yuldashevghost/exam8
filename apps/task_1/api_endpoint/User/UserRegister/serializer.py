from rest_framework import serializers

from apps.task_1.models import User


class UserRegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=8)
    email = serializers.EmailField()

    def validate_email(self, email):
        if self.instance:
            if User.objects.filter(email=email).exists():
                raise serializers.ValidationError("Email already registered")

        return email
