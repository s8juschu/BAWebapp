from django.contrib.auth import authenticate, logout, login as auth_login
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, reverse
from django.contrib.auth.models import User
from django.contrib import messages
from typing import Any

from . import models

def return_status(status):
    resp = HttpResponse()
    resp.status_code = status
    return resp

def registration(request):
    username = request.POST.get('user', None)
    user_exist = User.objects.filter(username=username).exists()
    if not user_exist:
        # create your user
        password = request.POST.get('pwd1', None)
        confirmpassword = request.POST.get('pwd2', None)
        email = request.POST.get('email', None)
        if confirmpassword != password:
            messages.info(request, 'Passwords did not match!', extra_tags='alert')
            return HttpResponseRedirect(reverse('index'))
        else:
            user = User.objects.create_user(username=username, password=password, email=email)
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
                messages.info(request, 'Username already exists!', extra_tags='alert')
                return HttpResponseRedirect(reverse('index'))
    else:
        messages.info(request, 'Username already exists!', extra_tags='alert')
        return HttpResponseRedirect(reverse('index'))


def login_view(request):
    user = request.POST.get('user', None)
    user_exist = User.objects.filter(username=user).exists()
    if user_exist:
        pwd = request.POST.get('pwd', None)
        if user is None or pwd is None:
            return return_status(418)
        user = authenticate(request=request, username=user, password=pwd)
        if user is not None and user.is_active:
            auth_login(request, user)
            return HttpResponseRedirect(reverse('home'))
        else:
            messages.info(request, 'Wrong username or password!', extra_tags='alert')
            return HttpResponseRedirect(reverse('index'))
    else:
        messages.info(request, 'Username not found!', extra_tags='alert')
        return HttpResponseRedirect(reverse('index'))


def logout_view(request):

    logout(request)
    return HttpResponseRedirect(reverse('index'))
