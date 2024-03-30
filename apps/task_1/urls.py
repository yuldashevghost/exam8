from django.urls import path

from apps.task_1.api_endpoint.User import UserCreateAPIView, UserListView, UserUpdateView, UserDestroyAPIView, \
    UserRetrieveAPIView, UserRegisterView, UserLoginAPIView

app_name = 'task_1'

urlpatterns = [
    path("user/register/", UserRegisterView.as_view()),
    path("user/login/", UserLoginAPIView.as_view()),
    path("user", UserListView.as_view()),
    path("user/create/", UserCreateAPIView.as_view()),
    path("user/<pk>/update/", UserUpdateView.as_view()),
    path("user/<pk>/delete/", UserDestroyAPIView.as_view()),
    path("user/<pk>/retrieve/", UserRetrieveAPIView.as_view()),

]