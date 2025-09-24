from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny

from apps.models import Register
from apps.serializers import RegisterModelSerializer


class RegisterListCreateAPIView(ListCreateAPIView):
    queryset = Register.objects.all()
    serializer_class = RegisterModelSerializer
    permission_classes = (AllowAny,)