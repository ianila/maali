from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

import jwt
from django.conf import settings
from datetime import datetime, timedelta

class MaaliUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None, **other_fields):
        if not email:
            raise ValueError('email connot be empty')

        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            **other_fields,
        )

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, first_name, last_name, password=None, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        
        return self.create_user(email, first_name, last_name, password, **other_fields)

class MaaliUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255, blank=False, null=False)
    last_name = models.CharField(max_length=255, blank=False, null=False)
    joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = MaaliUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.first_name

    @property
    def token(self):
        token = jwt.encode({'email': self.email, 'expire': 3600}, settings.SECRET_KEY, algorithm='HS256')
        return token
