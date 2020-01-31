from django.core.mail import send_mail

from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from stores.models import Store


def home(request):
    sts=Store.objects.all()

    return render(request, 'home.html',{"sts":sts},
                  )

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

        return redirect("/")

def sendemail(request):
    if request.method=="GET":
        fname = request.GET['fname']
        lname = request.GET['lname']
        email = request.GET['email']
        comment = request.GET['comment']

        str000 = "Name : "
        str0 = fname+" "+lname+" "
        str00 = "\n"
        str = email
        str3 = "Sent by :"
        str4 = "\n"
        str2 = comment
        str5 = "Feedback: "

    send_mail(fname,str000+str0+str00+str3+str+str4+str5+str2,email,['dafnowbd@gmail.com'])
    fail_silently = False
    return render(request,'contact2.html')
