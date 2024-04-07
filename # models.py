# models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_active = models.BooleanField(default=False)
    email_confirmation_token = models.CharField(max_length=255, null=True, blank=True)
