from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from . import forms
from .models import Store
from plans.models import Plan
from enrolments.models import Enrolment


# Create your views here.
def urStore(request):
    stores = Store.objects.filter(owner=request.user)
    return render(request, 'urstore.html', {'stores': stores})


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


def detail(request, store_id):
    status = 0

    detail_store = get_object_or_404(Store, pk=store_id)
    if detail_store.owner == request.user:
        status = 1
    pls = Plan.objects.filter(store=store_id)
    return render(request, 'detail_store.html',
                  {'detail_store': detail_store,
                   "s": status,
                   'pls': pls})


def shwoStore(request):
    sts = Store.objects.all()
    return render(request, 'showStore.html', {"sts": sts})


def shwoStorehm(request):
    sts = Store.objects.filter(category='HomeMade')
    return render(request, 'showStore.html', {"sts": sts})


def shwoStorepr(request):
    sts = Store.objects.filter(category='Professional')
    return render(request, 'showStore.html', {"sts": sts})


def dashboard(request):
    stores = Store.objects.filter(owner=request.user)
    print(stores)
    for i in stores:
        plans = Plan.objects.filter(store_id=i.id)
        print(plans)

        for j in plans:
            enrols = Enrolment.objects.filter(plan_id=j.id)
            print(enrols)
            return render(request, 'dahsboard.html', {"e": enrols})
    return render(request, "home2.html")


def update(request, x):
    tabup = Store.objects.get(pk=x)
    upform = forms.StoreForm(request.POST or None, request.FILES, instance=tabup)
    if upform.is_valid():
        upform.save()
        return redirect('/')
    return render(request, 'update.html',
                  {'form': upform,
                   "x": x})


def delete(r, tab_id):
    tab = Store.objects.get(pk=tab_id)
    tab.delete()
    return redirect("/")
