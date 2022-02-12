from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4

# Create your models here.
AGE_CHOICES = (
    ('Kid', 'Kid'),  # 0-13
    ('Teenager', 'Teenager'),  # 14-17
    ('Adult', 'Adult')  # 18+
)
MOVIE_TYPE = (
    ('Single', 'Single'),
    ('Seasonal', 'Seasonal')
)

class CustomUser(AbstractUser):
    profiles = models.ManyToManyField('Profile')


class Profile(models.Model):
    name = models.CharField(max_length=20)
    age_limit = models.CharField(max_length=9, choices=AGE_CHOICES)
    uuid = models.UUIDField(default=uuid4)

class Movie(models.Model):
    title = models.CharField(max_length=30, null=False, blank=False)
    age_limit = models.CharField(max_length=9, choices=AGE_CHOICES)
    description = models.CharField(max_length=200, null=True, blank=True)
    type = models.CharField(max_length=8, choices=MOVIE_TYPE)
    videos = models.ManyToManyField('Video')
    flyer = models.ImageField(upload_to='flyers')
    uuid = models.UUIDField(default=uuid4)
    #categories = models.ManyToManyField('Category', null=True, blank=True)

class Video(models.Model):
    title = models.CharField(max_length=30, null=True, blank=True)
    file = models.FileField(upload_to='movies')