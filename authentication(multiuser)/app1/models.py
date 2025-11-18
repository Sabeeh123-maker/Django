from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    phone = models.IntegerField(null=True)
    role = models.CharField(null=True)