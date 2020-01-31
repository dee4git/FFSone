from django.shortcuts import render, redirect, get_object_or_404
from .models import Plan
from . import forms
from stores.models import Store
from enrolments.models import Enrolment
# Create your views here.
def showPxS(request):
    plans=Plan.objects.all()
    return render(request,'showplanxstore.html',{"plans":plans})
def addPxS(request,store_id):
    print("in the method ID:",store_id)
    sts = Store.objects.filter(owner=request.user)

    if request.method == "POST":
        print("Entered")
        form = forms.PlanForm(request.POST, request.FILES)
        if form.is_valid():
            print("valid form")
            instance = form.save(commit=False)
            instance.store=Store.objects.get(pk=int(store_id))
            print("passed")
            instance.save()
            return redirect("/")
    else:
        form = forms.PlanForm()
        form.store=Store.objects.get(pk=int(store_id))


    return render(request, 'addplanxstore.html', {"form": form,
                                                  "sts":sts,
                                                  "sid":store_id})

def detail(request,plan_id):
    plan = get_object_or_404(Plan, pk=plan_id)
    enrl=Enrolment.objects.filter(enroller=request.user)
    return render(request, 'detailedplan.html', {'plan': plan,
                                                     'eid': enrl})