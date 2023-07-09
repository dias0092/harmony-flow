from django.db import models
from django.contrib.auth.models import User
from artists.models import Artist

class User(models.Model):
    REGULAR = 'Regular'
    PREMIUM = 'Premium'
    USER_TYPE_CHOICES = [
        (REGULAR, 'Regular'),
        (PREMIUM, 'Premium'),
    ]
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    profile_image = models.URLField(null=True)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default=REGULAR)

    def __str__(self):
        return self.name

class Follower(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.name} follows {self.artist.name}"