from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import reverse, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
import json

from website import views_user
from .models import Plan
from . import models

@login_required
def settinginfo(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('index'))
    if request.method == 'POST':
        user = request.user
        u = User.objects.filter(username=user)
        if user is not None:
            u.update(email=request.POST.get('email', None))
            u.update(first_name=request.POST.get('first_name', None))
            u.update(last_name=request.POST.get('last_name', None))

            messages.info(request, 'Settings successfully saved!', extra_tags='alert')
            return HttpResponseRedirect(reverse('settings'))
        else:
            views_user.return_status(500)

@login_required
def settingpwd(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('index'))
    if request.method == 'POST':
        user = request.user
        u = User.objects.filter(username=user)
        pwd1 = request.POST.get('pwd1', None)
        pwd2 = request.POST.get('pwd2', None)
        if pwd1 == pwd2:
            print(request.POST)
            if user is not None:
                user.set_password(pwd1)
                user.save()
                messages.info(request, 'New password successfully saved!', extra_tags='alert')
                update_session_auth_hash(request, request.user)
                return HttpResponseRedirect(reverse('settings'))
            else:
                views_user.return_status(500)
        else:
            messages.info(request, 'Password did not match!', extra_tags='alert')
            return HttpResponseRedirect(reverse('settings'))



#if `email1` is same as `email2`,

@login_required
def saveplan(request):
    getplaninfo = request.body
    planinfo = json.loads(getplaninfo)
    print(planinfo["poolsize"])
    return  HttpResponse(200)


@login_required
def showplan(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('index'))
    return Plan.objects.all()