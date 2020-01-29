from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from .models import Dguy
from .forms import cvForm
from .import forms

# def urguy(request):
#         stores = Dguy.objects.filter(owner=request.user)
#         return render(request, 'urstore.html', {'stores': stores})
def addguy(request):
    if request.method == "POST":
        form = forms.cvForm(request.POST, request.FILES)
        try:
            if form.is_valid():
                instance = form.save(commit=False)
                instance.boy = request.user
                instance.save()
                return redirect("/")
        except:
            return redirect("/")
    else:
        form = cvForm()
    return render(request, 'addcv.html', {"form": form})

def detail(request,dguy_id):
    dtguy = get_object_or_404(Dguy, pk=dguy_id)
    return render(request, 'detail_guy.html', {'dtguy': dtguy})

def shwoguy(request):
    dgs= Dguy.objects.all()
    return render(request, 'showdguys.html', {"dgs":dgs})
