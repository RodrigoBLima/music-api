from django.db import models
from artists.model import Artist
# Create your models here.

class Album(models.Model):
    album_name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)