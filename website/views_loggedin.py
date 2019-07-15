from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import reverse, render
from django.contrib.auth.decorators import login_required

from .models import Plan, PlanRow, Swimmer, Group
from . import models
from .forms import ContactForm
from django.core.mail import send_mail
from django.contrib import messages



@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def about(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # send email code goes here
            sender_name = form.cleaned_data['name']
            sender_email = form.cleaned_data['email']

            message = "{0} has sent you a new message:\n\n{1}".format(sender_name, form.cleaned_data['message'])
            send_mail('New Enquiry', message, sender_email, ['enquiry@exampleco.com'])

            messages.info(request, 'Your message was successfully send!', extra_tags='alert')

            return HttpResponseRedirect(reverse('aboutlog'))
    else:
        form = ContactForm()

    return render(request, 'aboutlog.html', {'form': form})

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
    if Plan.objects.filter(pk=plan_id).exists():
        plan = Plan.objects.get(pk=plan_id)
        if plan.user == request.user:
            rows = PlanRow.objects.filter(plan=plan)
            return render(request, 'showplan.html', context={'plan': plan, 'rows': rows, 'plan_id': plan_id})
        else:
            messages.info(request, 'Access denied. You are not the owner of this plan!', extra_tags='alert')
            return HttpResponseRedirect(reverse('manageplans'))
    else:
        messages.info(request, 'The plan with the id '+str(plan_id)+' does not exist.', extra_tags='alert')
        return HttpResponseRedirect(reverse('manageplans'))



@login_required
def alterplan(request, plan_id):
    if Plan.objects.filter(pk=plan_id).exists():
        plan = Plan.objects.get(pk=plan_id)
        if plan.user == request.user:
            rows = PlanRow.objects.filter(plan=plan)
            return render(request, 'alterplan.html', context={'plan': plan, 'rows': rows, 'plan_id': plan_id})
        else:
            messages.info(request, 'Access denied. You are not the owner of this plan!', extra_tags='alert')
            return HttpResponseRedirect(reverse('manageplans'))
    else:
        messages.info(request, 'The plan with the id '+str(plan_id)+' does not exist.', extra_tags='alert')
        return HttpResponseRedirect(reverse('manageplans'))




@login_required
def newathlete(request):
    return render(request, 'newathlete.html')

@login_required
def athletes(request):
    user = request.user
    swimmer = Swimmer.objects.filter(user=user)
    return render(request, 'athletes.html', context={'swimmer': swimmer})

@login_required
def group(request):
    user = request.user
    group = Group.objects.filter(user=user)
    return render(request, 'group.html', context={'group': group})

@login_required
def newgroup(request):
    return render(request, 'newgroup.html')

@login_required
def showathlete(request, athlete_id):
    if Swimmer.objects.filter(pk=athlete_id).exists():
        swimmer = Swimmer.objects.get(pk=athlete_id)
        if swimmer.user == request.user:
            return render(request, 'showathlete.html', context={'swimmer': swimmer, 'athlete_id': athlete_id})
        else:
            messages.info(request, 'Access denied. You are not the trainer of this athlete!', extra_tags='alert')
            return HttpResponseRedirect(reverse('group'))
    else:
        messages.info(request, 'The athlete with the id ' + str(athlete_id) + ' does not exist.', extra_tags='alert')
        return HttpResponseRedirect(reverse('group'))

@login_required
def alterathlete(request, athlete_id):
    if Swimmer.objects.filter(pk=athlete_id).exists():
        swimmer = Swimmer.objects.get(pk=athlete_id)
        if swimmer.user == request.user:
            return render(request, 'alteranathlete.html', context={'swimmer': swimmer, 'athlete_id': athlete_id})
        else:
            messages.info(request, 'Access denied. You are not the trainer of this athlete!', extra_tags='alert')
            return HttpResponseRedirect(reverse('group'))
    else:
        messages.info(request, 'The athlete with the id ' + str(athlete_id) + ' does not exist.', extra_tags='alert')
        return HttpResponseRedirect(reverse('group'))