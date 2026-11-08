from django.contrib import admin
from .forms import UserChangeForm, UserCreationForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from django.contrib.auth.models import Group
# Register your models here.


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    fieldsets = (
        ("Information User", {"fields":("username",)}),
    )

    add_fieldsets = (
        ("Create User", {"fields":("username","password1", "password2")}),
    )

    list_display = ["username"]

admin.site.unregister(Group)
admin.site.register(User, UserAdmin)
