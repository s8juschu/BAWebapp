from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import reverse, render

from . import models


def return_status(status):
    resp = HttpResponse()
    resp.status_code = status
    return resp


def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    else:
        return render(request, 'index.html')


def about(request):
    return render(request, 'aboutlog.html')

def newplan(request):
    return render(request, 'newplan.html')

def settings(request):
    user = request.user
    return render(request, 'settings.html', context={'user': user.username, 'email': user.email, 'first_name': user.first_name, 'last_name': user.last_name})

def help(request):
    return render(request, 'help.html')

def manageplans(request):
    return render(request, 'manageplans.html')

def group(request):
    return render(request, 'group.html')

def managegroups(request):
    return render(request, 'managegroups.html')
