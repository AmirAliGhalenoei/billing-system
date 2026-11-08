from django import forms
from .models import User
from django.contrib.auth.forms import (
    UserCreationForm as BaseUserCreationForm,
    UserChangeForm as BaseUserChangeForm
)


class UserCreationForm(BaseUserCreationForm):
    class Meta:
        model = User
        fields = BaseUserCreationForm.Meta.fields

class UserChangeForm(BaseUserChangeForm):
    class Meta:
        model = User
        fields = "__all__"
        