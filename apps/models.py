from django.contrib.auth.models import AbstractUser
from django.db.models import EmailField, CharField, BooleanField

from apps.managers import CustomUserManager


class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('client', 'Client'),
        ('user', 'User'),
    ]
    username = None
    first_name = None
    last_name = None

    email = EmailField(unique=True)
    name = CharField(max_length=255)
    is_active = BooleanField(default=False)
    role = CharField(max_length=20, choices=ROLE_CHOICES, default='user')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = CustomUserManager()

    def __str__(self):
        return f'{self.id} - {self.email}'
