from django.db import models
from albums.models import Album

class Track(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    duration = models.IntegerField(null=True, blank=True)
    audio_file = models.FileField(upload_to='static/tracks/')

    def __str__(self):
        return self.name
