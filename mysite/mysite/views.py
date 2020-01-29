from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect

from stores.models import Store


def home(request):
    sts=Store.objects.all()
    return render(request, 'home.html',{"sts":sts})

#@login_required(login_url="/acc/login/")
def makemoney(request):
    return render(request, 'makemoneypage.html')


def contact(request):
    return render(request, 'contact.html')

def send_email(request):
    if request.method == "GET":
        fname = request.GET['fname']
        lname = request.GET['lname']
        email = request.GET['email']
        comment = request.GET['comment']
        if fname and lname and email and comment:
            try:
                send_mail(fname, lname, email,comment, ['dee4code@gmail.com'])
                print("mail sent")
            except BadHeaderError:
                return HttpResponse('Invalid header found.')

            return redirect('/')
        else:
            # In reality we'd use a form class
            # to get proper validation errors.
            return HttpResponse('Make sure all fields are entered and valid.')