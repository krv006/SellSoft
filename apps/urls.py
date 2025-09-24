from django.urls import path

from apps.views import RegisterListCreateAPIView

urlpatterns = [
    path('', RegisterListCreateAPIView.as_view()),
]
