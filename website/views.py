from django.shortcuts import render, reverse
from .forms import ContactForm
from django.core.mail import send_mail
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect

def index (request):
    return render(request, 'index.html')

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

            return HttpResponseRedirect(reverse('about'))
    else:
        form = ContactForm()

    return render(request, 'about.html', {'form': form})