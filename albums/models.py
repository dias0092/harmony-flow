from django.db import models
from artists.models import Artist
from harmonyflow.storage_backends import AzureMediaStorage


class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    image = models.ImageField(upload_to='albums/', storage=AzureMediaStorage())

    def __str__(self):
        return self.name