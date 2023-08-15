from django.db import models
from users.models import User
from tracks.models import Track
from harmonyflow.storage_backends import AzureMediaStorage

class Playlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='playlist_images/', storage=AzureMediaStorage(), null=True, blank=True)

    def __str__(self):
        return self.name

class PlaylistTrack(models.Model):
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    order = models.IntegerField()

    def __str__(self):
        return f"{self.playlist.name} - {self.track.name}"