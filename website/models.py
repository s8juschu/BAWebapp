from django.db import models
from django.contrib.auth.models import User



class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE, default=None)
    username = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30, blank=True, default='')
    last_name = models.CharField(max_length=30, blank=True, default='')

    #def __str__(self):
    #    return self.username