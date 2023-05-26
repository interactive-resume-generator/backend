from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import UserCreate, UserChange
from .models import User


class CustomUserAdmin(UserAdmin):
    add_form = UserCreate
    form = UserChange
    model = User
    list_display = [
        "email",
        "username",
    ]


admin.site.register(User, CustomUserAdmin)
