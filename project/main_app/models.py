from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(unique=True)
    avatar = models.ImageField(upload_to='avatars')
    sex = models.BooleanField()
    username = None

    matches = models.ManyToManyField('main_app.User')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
