from django.contrib.auth import authenticate
from rest_framework import serializers


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(style={"input_type": "password"})

    def validate(self, data):
        username = data.get("username")
        password = data.get("password")

        if username and password:
            user = authenticate(username=username, password=password)
            if user is None:
                raise serializers.ValidationError("Username or Password is incorrect")

        else:
            raise serializers.ValidationError("Missing username or password")

        data["user"] = user
        return data
