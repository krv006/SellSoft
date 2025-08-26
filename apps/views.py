from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.generics import ListAPIView, GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from apps.models import User
from apps.serializers import UserModelSerializer, RegisterUserModelSerializer, LoginUserModelSerializer


@extend_schema(tags=["Users"])
class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


@extend_schema(tags=['Auth'], description="""
API for verify code
""")
class RegisterUserView(GenericAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterUserModelSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = RegisterUserModelSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(
                {
                    "message": "User registered successfully!",
                    "user_id": user.id,
                    "email": user.email
                },
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(tags=['Auth'], description="""
API for verify code
""")
class LoginAPIView(GenericAPIView):
    serializer_class = LoginUserModelSerializer
    permission_classes = AllowAny,
    authentication_classes = []

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_200_OK)
