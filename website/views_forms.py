from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import reverse, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
import json

from website import views_user
from .models import Plan, PlanRow, Swimmer
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
    totaldistance = planinfo["totaldistance"]

    user = request.user
    u = User.objects.get(username=user)

    planmodel = Plan()
    planmodel.name = planname
    planmodel.size = poolsize
    planmodel.totaldistance = totaldistance
    planmodel.user = u
    planmodel.save()
    listitem = planinfo["listarray"]
    print(repr(listitem))
    for item in listitem:
        planrow = PlanRow(rep1=item["rep1"],rep2=item["rep2"],distance=item["distance"],resttime=item["resttime"],resttype=item["resttype"],style=item["style"],comments=item["comments"],tools=item["tools"], effort=item["effort"])
        planrow.plan = planmodel
        #print(item)
        planrow.save()

    return HttpResponse(200)

def deleteplan(request, plan_id):
    plan = Plan.objects.get(pk=plan_id)
    rows = PlanRow.objects.filter(plan=plan).delete()
    plan.delete()
    return HttpResponseRedirect(reverse('manageplans'))

@login_required
def updateplan(request, plan_id):

    #delte old planrows
    plan = Plan.objects.get(pk=plan_id)
    PlanRow.objects.filter(plan=plan).delete()

    #get request payload
    getplaninfo = request.body.decode('utf-8')
    planinfo = json.loads(getplaninfo)

    #save payload to Plan database
    planname= planinfo["planname"]
    poolsize = planinfo["poolsize"]
    totaldistance = planinfo["totaldistance"]


    planmodel = Plan.objects.get(pk=plan_id)
    planmodel.name = planname
    planmodel.size = poolsize
    planmodel.totaldistance = totaldistance
    planmodel.save()

    listitem = planinfo["listarray"]
    for item in listitem:
        planrow = PlanRow(rep1=item["rep1"], rep2=item["rep2"], distance=item["distance"], resttime=item["resttime"],
                          resttype=item["resttype"], style=item["style"], comments=item["comments"],
                          tools=item["tools"], effort=item["effort"])
        planrow.plan = planmodel
        planrow.save()

    return HttpResponse(200)





@login_required
def saveathlete(request):

    #get request payload
    getathleteinfo = request.body.decode('utf-8')
    athleteinfo = json.loads(getathleteinfo)

    #save payload to Plan database
    firstname= athleteinfo["firstname"]
    lastname = athleteinfo["lastname"]
    email = athleteinfo["email"]
    birthdate = athleteinfo["birthdate"]
    group = athleteinfo["group"]
    info = athleteinfo["info"]

    user = request.user
    u = User.objects.get(username=user)

    swimmer = Swimmer()
    swimmer.first_name = firstname
    swimmer.last_name = lastname
    swimmer.email = email
    swimmer.birthdate = birthdate
    swimmer.group = group
    swimmer.info = info
    swimmer.user = u
    swimmer.save()

    return HttpResponse(200)

def deleteathlete(request, athlete_id):
    swimmer = Swimmer.objects.filter(pk=athlete_id).delete()
    return HttpResponseRedirect(reverse('group'))


@login_required
def updateathlete(request, athlete_id):

    #get request payload
    getathleteinfo = request.body.decode('utf-8')
    athleteinfo = json.loads(getathleteinfo)

    #save payload to Plan database
    firstname= athleteinfo["firstname"]
    lastname = athleteinfo["lastname"]
    email = athleteinfo["email"]
    birthdate = athleteinfo["birthdate"]
    group = athleteinfo["group"]
    info = athleteinfo["info"]


    swimmer = Swimmer.objects.get(pk=athlete_id)
    swimmer.first_name = firstname
    swimmer.last_name = lastname
    swimmer.email = email
    swimmer.birthdate = birthdate
    swimmer.group = group
    swimmer.info = info
    swimmer.save()

    return HttpResponse(200)



