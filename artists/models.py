from django.db import models
from harmonyflow.storage_backends import AzureMediaStorage

class Artist(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100, null=True, blank=True)
    image = models.URLField(upload_to='artist_images/', storage=AzureMediaStorage(), null=True, blank=True)

    def __str__(self):
        return self.name
