from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from stores.models import Store
from enrolments.models import Enrolment
# Create your views here.
def reg(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username taken")
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email in use")

            else:
                user = User.objects.create_user(username=username, password=password2, email=email,
                                                first_name=first_name, last_name=last_name)
                user.save()
                print("user created sir")
                return redirect('login')
        else:
            messages.info(request, 'pass not mathcing')
            return redirect('reg')

    return render(request, 'reg.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, "invalid")
            return redirect('login')
    else:

        return render(request, 'login2.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def myprofile(request):
    sts = Store.objects.filter(owner=request.user)
    els=Enrolment.objects.filter(enroller=request.user)
    return render(request, 'myprofile.html', {
        "sts":sts,
        "els":els,
    })
