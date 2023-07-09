from django.db import models
from artists.models import Artist
from users.models import User

class Follower(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.name} follows {self.artist.name}"
