from django.db import models
from artists.models import Artist

class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    image = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name