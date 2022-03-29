import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from uuid import uuid4

# Create your models here.
AGE_CHOICES = (
    ('Kids', 'Kids'),  # 7+
    ('Teenagers', 'Teenagers'),  # 13+
    ('Adults', 'Adults')  # 18+
)
MOVIE_TYPE = (
    ('Single', 'Single'),
    ('Seasonal', 'Seasonal')
)
YEAR = datetime.datetime.now().year + 3  # Max year of possible movie productions


class CustomUser(AbstractUser):
    profiles = models.ManyToManyField('Profile')


class Profile(models.Model):
    name = models.CharField(max_length=20)
    age_limit = models.CharField(max_length=9, choices=AGE_CHOICES)
    uuid = models.UUIDField(default=uuid4)


class Movie(models.Model):
    title = models.CharField(max_length=30, null=False, blank=False)
    age_limit = models.CharField(max_length=9, choices=AGE_CHOICES)
    description = models.CharField(max_length=500, null=True, blank=True)
    year_of_production = models.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(YEAR)], blank=True, null=True)
    type = models.CharField(max_length=8, choices=MOVIE_TYPE)
    num_of_seasons = models.IntegerField(null=True, blank=True)
    videos = models.ManyToManyField('Video')
    flyer = models.ImageField(upload_to='flyers', null=True, blank=True)
    uuid = models.UUIDField(default=uuid4)
    genres = models.ManyToManyField('Genre')


class Video(models.Model):
    title = models.CharField(max_length=30, null=True, blank=True)
    seasonal = models.BooleanField(default=False)
    season = models.IntegerField(validators=[MinValueValidator(1)], blank=True, null=True, default=None)
    episode = models.IntegerField(validators=[MinValueValidator(1)], blank=True, null=True, default=None)
    file = models.FileField(upload_to='movies')


class Genre(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)

