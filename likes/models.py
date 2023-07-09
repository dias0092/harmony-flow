from django.db import models
from users.models import User
from tracks.models import Track

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    like_date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.name} likes {self.track.name}"
