from django.shortcuts import render,redirect
from.import forms
from plans.models import Plan
from.models import Enrolment
# Create your views here.
def addEnrl(request, plan_id):
    if request.method == "POST":
        print("Entered")
        form = forms.EnrolmentForm(request.POST, request.FILES)
        if form.is_valid():
            print("valid form")
            instance = form.save(commit=False)
            instance.enroller = request.user
            instance.plan = Plan.objects.get(pk=int(plan_id))
            print("passed")
            instance.save()
            return redirect("/")
    else:
        form = forms.EnrolmentForm()
        form.plan = Plan.objects.get(pk=int(plan_id))

    return render(request, 'addenrl.html', {"form": form,
                                                  "eid": plan_id})
