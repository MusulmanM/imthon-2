from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "admin"
        DENTISTS = "DENTISTS", "doctor"
        CLIENT = "CLIENT", "client"

    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)

    groups = models.ManyToManyField(
        "auth.Group", related_name="custom_user_groups", blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission", related_name="custom_user_permissions", blank=True
    )
