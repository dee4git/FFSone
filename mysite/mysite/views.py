from django.core.mail import send_mail

from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from stores.models import Store


def home(request):
    sts=Store.objects.all()
    return render(request, 'home.html',{"sts":sts})

#@login_required(login_url="/acc/login/")
def makemoney(request):
    return render(request, 'makemoneypage.html')


def contact(request):
    return render(request, 'contact.html')
def sendInfo(request):
    if request.method=="GET":
        fname = request.GET['fname']
        lname = request.GET['lname']
        email = request.GET['email']
        comment = request.GET['comment']
        print(fname)
        print(lname)
        print(email)
        print(comment)

        send_mail(
            'Subject here',
            'Here is the message.',
            email,
            ['dee4code@gmail.com'],
            fail_silently=False,
        )

        return redirect("/")