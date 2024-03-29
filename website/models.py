from django.db import models
from django.contrib.auth.models import User



class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE, default=None)
    username = models.CharField(max_length=30, unique=True)
    email = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30, blank=True, null=True,  default='')
    last_name = models.CharField(max_length=30, blank=True, null=True, default='')

class Plan(models.Model):
    name = models.CharField(max_length=128)
    size = models.CharField(max_length=30)
    totaldistance = models.IntegerField(default=0)
    saved_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class PlanRow(models.Model):
    rep1 = models.IntegerField(default=1)
    rep2 = models.IntegerField(default=1)
    distance = models.IntegerField(default=0)
    resttype = models.CharField(max_length=30)
    resttime = models.CharField(max_length=10, null=True)
    style = models.CharField(max_length=30)
    comments = models.CharField(max_length=828, null=True)
    tools = models.CharField(max_length=30)
    effort = models.IntegerField(default=0)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)

class Group(models.Model):
    name = models.CharField(max_length=30)
    num = models.IntegerField(default=0)
    starttime = models.CharField(max_length=25, default='')
    endtime = models.CharField(max_length=25, default='')
    comments = models.CharField(max_length=828, null=True)
    place = models.CharField(max_length=255, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Swimmer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birthdate = models.CharField(max_length=30, null=True, default='')
    email = models.CharField(max_length=30)
    info = models.CharField(max_length=828, null=True, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class RelationsSwimGroup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    swimmer = models.ForeignKey(Swimmer, on_delete=models.CASCADE)



