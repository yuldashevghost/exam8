from django.urls import path

from apps.user.api_endpoint.User import (
    UserCreateAPIView,
    UserListView,
    UserUpdateView,
    UserDestroyAPIView,
    UserRetrieveAPIView,
    UserRegisterView,
    UserLoginAPIView,
    UserLogoutAPIView,
)

app_name = "user"

urlpatterns = [
    path("user/register/", UserRegisterView.as_view()),
    path("user/login/", UserLoginAPIView.as_view()),
    path("user/logout/", UserLogoutAPIView.as_view()),
    path("user", UserListView.as_view()),
    path("user/create/", UserCreateAPIView.as_view()),
    path("user/<pk>/update/", UserUpdateView.as_view()),
    path("user/<pk>/delete/", UserDestroyAPIView.as_view()),
    path("user/<pk>/retrieve/", UserRetrieveAPIView.as_view()),
]
