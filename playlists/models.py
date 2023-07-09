from django.db import models
from users.models import User

class Playlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name
