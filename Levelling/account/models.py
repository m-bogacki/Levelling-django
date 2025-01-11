from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.contrib.auth.hashers import make_password


class Address(models.Model):
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=60)


class Progress(models.Model):
    level = models.IntegerField(default=1, max_length=100)
    experience = models.IntegerField(default=0)


class User(AbstractUser):
    USER = 1
    ADMIN = 2

    ROLE_CHOICES = ((USER, "User"), (ADMIN, "Admin"))
    role = models.PositiveSmallIntegerField(
        default=1, choices=ROLE_CHOICES, blank=True, null=True
    )
    address = models.OneToOneField(
        Address, on_delete=models.CASCADE, blank=True, null=True
    )
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    progress = models.OneToOneField(
        Progress, on_delete=models.CASCADE, blank=True, null=True
    )

    def __str__(self):
        return self.username
