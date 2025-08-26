from django.urls import path

from apps.views import UserListAPIView, RegisterUserView, LoginAPIView

urlpatterns = [
    # todo user
    path('user', UserListAPIView.as_view(), name='user-list'),
    path('register/', RegisterUserView.as_view(), name='user-register'),
    path("login/", LoginAPIView.as_view(), name="user-login"),
]
