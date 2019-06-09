from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import reverse, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
import json

from website import views_user
from .models import Plan, PlanRow, UserProfile
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


@login_required
def saveplan(request):

    #get request payload
    getplaninfo = request.body.decode('utf-8')
    planinfo = json.loads(getplaninfo)

    #save payload to Plan database
    planname= planinfo["planname"]
    poolsize = planinfo["poolsize"]

    #user = request.user
    #u = UserProfile.objects.get(username=user)

    #planmodel = Plan()
    #planmodel.name = planname
    #planmodel.size = poolsize
    #planmodel.user = u
    #planmodel.save()
    #print("Planname: " + planname)
    #print("Poolsize: " + poolsize)
    #listitem = planinfo["listarray"]
    #for item in listitem:
    #    planrow = PlanRow()
    #    planrow.plan = planmodel
    #    #print(item)
    #    for key, value in item.items():
    #        print(key + ": " + value)
    #        planrow.key =  value
    #    planrow.save()

    return  HttpResponse(200)


@login_required
def showplan(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('index'))
    return Plan.objects.all()