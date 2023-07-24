from django.db import models
from albums.models import Album
from artists.models import Artist
from mutagen.mp3 import MP3
from .validators import validate_is_audio

class Track(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, related_name='tracks', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    duration = models.IntegerField(null=True, blank=True)
    audio_file = models.FileField(upload_to='tracks/', validators=[validate_is_audio])

    def __str__(self):
        return self.name
