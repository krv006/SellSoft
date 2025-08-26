from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.fields import EmailField
from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework_simplejwt.tokens import RefreshToken

from apps.models import User


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


from django.contrib.auth.hashers import make_password
from rest_framework.serializers import CharField, ValidationError


class RegisterUserModelSerializer(ModelSerializer):
    confirm_password = CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            'email',
            'password',
            'confirm_password',
        )
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, attrs):
        confirm_password = attrs.pop('confirm_password')
        password = attrs.get('password')
        if confirm_password != password:
            raise ValidationError("Passwords did not match!")

        attrs['password'] = make_password(password)
        return attrs


class LoginUserModelSerializer(Serializer):
    email = EmailField()
    password = CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise ValidationError("Bunday email mavjud emas bizda")

        if not user.check_password(password):
            raise ValidationError("Password ni xato kiritdingiz !!!")
        if not user.is_active:
            user.is_active = True
            user.save(update_fields=['is_active'])
        attrs['user'] = user
        return attrs