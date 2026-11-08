from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import UserManager
# Create your models here.


class User(AbstractUser):
    first_name = None
    last_name = None
    email = None

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.username

    
