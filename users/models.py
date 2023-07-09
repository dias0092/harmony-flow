import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    REGULAR = 'Regular'
    PREMIUM = 'Premium'
    USER_TYPE_CHOICES = [
        (REGULAR, 'Regular'),
        (PREMIUM, 'Premium'),
    ]
    username = models.CharField(max_length=150, unique=True, default=uuid.uuid4)
    date_of_birth = models.DateField(null=True, blank=True)
    profile_image = models.URLField(null=True, blank=True)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default=REGULAR)
