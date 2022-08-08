from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    age = models.CharField(max_length=3, blank=True, null=True)
    gender = models.CharField(max_length=1, blank=True, null=True)
    nickname = models.CharField(max_length=25, blank=True, null=True)

    def __str__(self):
        return self.email
