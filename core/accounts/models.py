from turtle import update
from venv import create
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser,PermissionsMixin)

class User(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(max_length=255, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    #is_verified = models.BooleanField(default=False)

    created_date=models.DateField(auto_now_add=True)
    updated_date=models.DateField(auto_now=True)

    #USERNAME_FIELD = 'email'
    first_name=models.CharField(max_length=255)
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email



