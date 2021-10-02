from django.db import models
from artists.models import Artist
# Create your models here.

class Album(models.Model):
    album_name = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return self.album_name
    class Meta:
        ordering = ['album_name']