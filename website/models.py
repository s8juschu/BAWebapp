from django.db import models
from django.contrib.auth.models import User



class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE, default=None)
    username = models.CharField(max_length=30, unique=True)
    email = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30, blank=True, null=True,  default='')
    last_name = models.CharField(max_length=30, blank=True, null=True, default='')

    #def __str__(self):
    #    return self.username

class Plan(models.Model):
    name = models.CharField(max_length=128)
    size = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class PlanRow(models.Model):
    rep1 = models.IntegerField()
    rep2 = models.IntegerField()
    distance = models.IntegerField()
    resttype = models.CharField(max_length=30)
    resttime = models.CharField(max_length=10,null=True)
    style = models.CharField(max_length=30)
    comments = models.CharField(max_length=828, null=True)
    tools = models.CharField(max_length=30)
    effort = models.IntegerField()
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)


class Swimmer(models.Model):
    email = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)


