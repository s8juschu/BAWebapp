from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import reverse, render
from django.contrib.auth.decorators import login_required

from .models import Plan, PlanRow, Swimmer
from . import models


@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def about(request):
    return render(request, 'aboutlog.html')

@login_required
def settings(request):
    user = request.user
    return render(request, 'settings.html', context={'user': user.username, 'email': user.email, 'first_name': user.first_name, 'last_name': user.last_name})

@login_required
def help(request):
    return render(request, 'help.html')




@login_required
def newplan(request):
    return render(request, 'newplan.html')


@login_required
def manageplans(request):
    user = request.user
    plans = Plan.objects.filter(user=user)
    return render(request, 'manageplans.html', context={'obj': plans})

@login_required
def showplan(request, plan_id):
    plan = Plan.objects.get(pk=plan_id)
    rows = PlanRow.objects.filter(plan=plan)
    return render(request, 'showplan.html', context={'plan': plan, 'rows': rows, 'plan_id': plan_id})


@login_required
def alterplan(request, plan_id):
    plan = Plan.objects.get(pk=plan_id)
    rows = PlanRow.objects.filter(plan=plan)
    return render(request, 'alterplan.html', context={'plan': plan, 'rows': rows, 'plan_id': plan_id})




@login_required
def newathlete(request):
    return render(request, 'newathlete.html')

@login_required
def group(request):
    user = request.user
    swimmer = Swimmer.objects.filter(user=user)
    return render(request, 'group.html', context={'swimmer': swimmer})

@login_required
def showathlete(request, athlete_id):
    swimmer = Swimmer.objects.get(pk=athlete_id)
    return render(request, 'showathlete.html', context={'swimmer': swimmer, 'athlete_id': athlete_id})

@login_required
def alterathlete(request, athlete_id):
    swimmer = Swimmer.objects.get(pk=athlete_id)
    return render(request, 'alteranathlete.html', context={'swimmer': swimmer, 'athlete_id': athlete_id})