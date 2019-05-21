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
    return render(request, 'settings.html')

def help(request):
    return render(request, 'help.html')
