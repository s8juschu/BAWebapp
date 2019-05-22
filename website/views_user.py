from django.contrib.auth import authenticate, logout, login as auth_login
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, reverse
from django.contrib.auth.models import User
from django.contrib import messages

from . import models

def return_status(status):
    resp = HttpResponse()
    resp.status_code = status
    return resp

def registration(request):
    username = request.POST.get('user', None)
    password = request.POST.get('pwd1', None)
    #confirmpassword = request.POST.get('pwd2', None)
    email = request.POST.get('email', None)
    user = User.objects.create_user(username=username, password=password)
    #if confirmpassword != password:
    #    return
    if user is not None:
        user.save()
        user_profile = models.UserProfile()
        user_profile.username = username
        user_profile.email = email
        user_profile.user = user
        user_profile.save()
        auth_login(request, user)
        return HttpResponseRedirect(reverse('home'))
    else:
        return_status(500)


def login_view(request):
    user = request.POST.get('user', None)
    pwd = request.POST.get('pwd', None)
    if user is None or pwd is None:
        return return_status(418)
    user = authenticate(request=request, username=user, password=pwd)
    if user is not None and user.is_active:
        auth_login(request, user)
        return HttpResponseRedirect(reverse('home'))
    else:
        return return_status(418)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))
