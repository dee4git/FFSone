from django.shortcuts import render, redirect
from . import forms
from .models import Store

# Create your views here.
def addStore(request):
    if request.method == "POST":
        form = forms.StoreForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.owner = request.user
            instance.save()
            return redirect("/")
    else:
        form = forms.StoreForm()
    return render(request, 'addStore.html', {"form": form})


def shwoStore(request):
    sts= Store.objects.all()
    return render(request, 'showStore.html', {"sts":sts})
