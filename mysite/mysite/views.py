from django.core.mail import send_mail
from django.db.models import Q

from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from stores.models import Store
from plans.models import Plan


def search(request):
    if request.method == 'GET':  # If the form is submitted
        kw = request.GET.get('search_box', None)
        str="no results found\n"
        s1=   "Search suggestions:\n"
        s2=    "-Your location [eg: Farmgate]\n"
        s3=    "-Food item [eg: Rice, Chicken]\n"
        s4=    "-Category [eg: Premium]\n"
        plans=[]
        stores=[]
        if kw :

            plans = Plan.objects.filter(Q(name__contains=kw)|
                                        Q(category__contains=kw)|
                                        Q(mealDescription__contains=kw)
                                        )
            stores = Store.objects.filter(Q(name__contains=kw) |
                                        Q(category__contains=kw) |
                                        Q(description__contains=kw) |
                                        Q(phone__contains=kw) |
                                        Q(location__contains=kw)
                                        )
            if plans or stores:
                return render(request, 'search.html',{
                    "kw": kw,
                    "plans": plans,
                    "sts": stores,
                                           } )
        print(plans)
        print(stores)
    return render(request, 'search.html', {"kw": kw, "str": str,
                                           "s1":s1,
                                           "s2":s2,
                                           "s3":s3,
                                           "s4":s4,
                                           })


def home(request):
    sts = Store.objects.all()

    return render(request, 'home.html', {"sts": sts},
                  )


# @login_required(login_url="/acc/login/")
def makemoney(request):
    return render(request, 'makemoneypage.html')


def contact(request):
    return render(request, 'contact.html')


def sendInfo(request):
    if request.method == "GET":
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
    if request.method == "GET":
        fname = request.GET['fname']
        lname = request.GET['lname']
        email = request.GET['email']
        comment = request.GET['comment']

        str000 = "Name : "
        str0 = fname + " " + lname + " "
        str00 = "\n"
        str = email
        str3 = "Sent by :"
        str4 = "\n"
        str2 = comment
        str5 = "Feedback: "

    send_mail(fname, str000 + str0 + str00 + str3 + str + str4 + str5 + str2, email, ['dafnowbd@gmail.com'])
    fail_silently = False
    return render(request, 'contact2.html')
