from django.contrib.auth.models import AbstractUser, User
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=50, default=' ')
    city = models.CharField(max_length=50, default=' ')
    state = models.CharField(max_length=50, default='NE')
    zipcode = models.CharField(max_length=10, default='00000')
    phone = models.CharField(max_length=20, default='(402)000-0000')
    username = models.CharField(max_length=8, unique=True, verbose_name='NUID', default='00000000')
