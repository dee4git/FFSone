from django.shortcuts import render, redirect
from .models import Plan
from . import forms
from stores.models import Store
# Create your views here.
def showPxS(request):
    plans=Plan.objects.all()
    return render(request,'showplanxstore.html',{"plans":plans})
def addPxS(request):

    sts = Store.objects.filter(owner=request.user)

    if request.method == "POST":

        form = forms.PlanForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect("/")
    else:
        form = forms.PlanForm()


    return render(request, 'addplanxstore.html', {"form": form,"sts":sts})