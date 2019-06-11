from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import reverse, render
from django.contrib.auth.decorators import login_required

from .models import Plan, PlanRow
from . import models


@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def about(request):
    return render(request, 'aboutlog.html')

@login_required
def newplan(request):
    return render(request, 'newplan.html')

@login_required
def settings(request):
    user = request.user
    return render(request, 'settings.html', context={'user': user.username, 'email': user.email, 'first_name': user.first_name, 'last_name': user.last_name})

@login_required
def help(request):
    return render(request, 'help.html')

@login_required
def manageplans(request):
    return render(request, 'manageplans.html', context={'obj': Plan.objects.all()})

@login_required
def group(request):
    return render(request, 'group.html')

@login_required
def managegroups(request):
    return render(request, 'managegroups.html')
