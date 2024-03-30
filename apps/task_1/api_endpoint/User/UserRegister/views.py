from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.task_1.api_endpoint.User.UserRegister.serializer import UserRegisterSerializer
from apps.task_1.models import User


class UserRegisterView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data.get("username")
            password = serializer.validated_data.get("password")
            email = serializer.validated_data.get("email")
            old_user = User.objects.filter(email=email).first()
            if old_user:
                if old_user.deleted:
                    old_user.deleted = False
                    old_user.save()
                else:
                    return Response(
                        serializer.errors, status=status.HTTP_400_BAD_REQUEST
                    )
            user = User.objects.create(username=username, email=email)
            user.set_password(password)
            user.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


__all__ = ["UserRegisterView"]
