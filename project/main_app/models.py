from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.gis.db.models import PointField
from django.core.mail import send_mail
from django.db import models


class User(AbstractUser):
    email = models.EmailField(unique=True)
    avatar = models.ImageField(upload_to='avatars')
    sex = models.BooleanField()
    location = PointField(srid=4326, geography=True)
    username = None

    matches = models.ManyToManyField('main_app.User', related_name='matched')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def notify(self, email):
        send_mail('Новая симпатия', f'Вы понравились {email}', settings.EMAIL_HOST_USER, [self.email])
