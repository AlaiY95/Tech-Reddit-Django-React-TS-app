from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Overriding Class User in site-packages/django/contrib/auth/models.py
class User(AbstractUser):
    USERNAME_FIELD = 'email'
    # email is unique as we validate users based on email
    email = models.EmailField(blank=True, unique=True)

    REQUIRED_FIELDS = ['username']