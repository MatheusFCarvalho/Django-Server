from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    sector = models.CharField(max_length=100, blank=True)
    trustly = models.BooleanField(default=False)

    def __str__(self):
        return self.username

    def get_name_capitalized(self):
        return (self.first_name + ' ' + self.last_name).capitalize