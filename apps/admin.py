from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.models import Register


@admin.register(Register)
class RegisterAdmin(ModelAdmin):
    pass
