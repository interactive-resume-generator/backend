from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class UserCreate(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email")


class UserChange(UserChangeForm):
    class Meta:
        model = User
        fields = ("username", "email")