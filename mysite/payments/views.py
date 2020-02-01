from django.shortcuts import render,redirect
from .import forms
from .models import Payment
from enrolments.models import Enrolment
from plans.models import Plan
from enrolments import views
# Create your views here.
def pay(request,enl_id):

    if request.method == "POST":
        global pr
        pr=views.rp()
        form = forms.PayForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.enrolment = Enrolment.objects.get(pk=int(enl_id))
            instance.save()
            return redirect("/")
    else:
        form = forms.PayForm()

    return render(request, 'pay.html', {"form": form,
                                        "price":pr,
                                        "enl_id":enl_id})

