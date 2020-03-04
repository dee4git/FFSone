from django.shortcuts import render, redirect, get_object_or_404
from .models import Plan
from . import forms
from stores.models import Store
from enrolments.models import Enrolment, Rating
from statistics import mean


# Create your views here.

def regular(request):
    plans = Plan.objects.filter(category='Regular')
    return render(request, 'showplanxstore.html', {"plans": plans})


def regular1(request):
    plans = Plan.objects.filter(category='Exclusive')
    return render(request, 'showplanxstore.html', {"plans": plans})


def regular2(request):
    plans = Plan.objects.filter(category='Premium')
    return render(request, 'showplanxstore.html', {"plans": plans})


def showphtl(request):
    plans = Plan.objects.order_by('-price')
    return render(request, 'showplanxstore.html', {"plans": plans})


def showphtl2(request):
    plans = Plan.objects.order_by('price')
    return render(request, 'showplanxstore.html', {"plans": plans})


def showPxS(request):
    plans = Plan.objects.all()
    return render(request, 'showplanxstore.html', {"plans": plans})


def addPxS(request, store_id):
    print("in the method ID:", store_id)
    sts = Store.objects.filter(owner=request.user)

    if request.method == "POST":
        print("Entered")
        form = forms.PlanForm(request.POST, request.FILES)
        if form.is_valid():
            print("valid form")
            instance = form.save(commit=False)
            instance.store = Store.objects.get(pk=int(store_id))
            print("passed")
            instance.save()
            return redirect("/")
    else:
        form = forms.PlanForm()
        form.store = Store.objects.get(pk=int(store_id))

    return render(request, 'addplanxstore.html', {"form": form,
                                                  "sts": sts,
                                                  "sid": store_id})


def Average(lst):
    return mean(lst)


def detail(request, plan_id):
    rs = Rating.objects.filter(plan=int(plan_id))
    nl = []

    rating = 0

    t = 0
    for i in rs:
        # ovreall
        t += 1
        nl.append(i.rating)
        rating = round(Average(nl), 2)
    plan = get_object_or_404(Plan, pk=plan_id)
    status = 0

    if plan.store.owner == request.user:
        status = 1
    return render(request, 'detailedplan.html', {'plan': plan,
                                                 't': t,
                                                 'rs': rs,
                                                 'plan': plan,
                                                 'rating': rating,
                                                 "s": status})


def update(request, x):
    tabup = Plan.objects.get(pk=x)
    upform = forms.PlanForm(request.POST or None, request.FILES, instance=tabup)
    if upform.is_valid():
        upform.save()
        return redirect('/')
    return render(request, 'updateplan.html',
                  {'form': upform,
                   "x": x})


def delete(r, tab_id):
    tab = Plan.objects.get(pk=tab_id)
    tab.delete()
    return redirect("/")
