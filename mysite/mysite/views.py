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
    return render()