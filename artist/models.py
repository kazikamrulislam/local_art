from django.db import models
from django.contrib.auth.models import AbstractUser

class Artist(AbstractUser):
    artist_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    bio = models.TextField(blank=True)
    password = models.CharField(max_length=100)
    username = None
    first_name = None
    last_name = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []