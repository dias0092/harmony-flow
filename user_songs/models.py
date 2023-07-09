from django.db import models
from users.models import User
from tracks.models import Track

class UserSong(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(Track, on_delete=models.CASCADE)
    play_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.name} played {self.song.name}"
