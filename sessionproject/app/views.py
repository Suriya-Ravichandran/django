from django.shortcuts import render,redirect
from .forms import SigninForm
# Create your views here.


def login(request):
    if request.method == 'POST':
        username=request.POST.get("username")
        password=request.POST.get("password")
        request.session["username"]=username
        request.session["password"]=password
        return redirect('app:home')

    return render(request,"index.html")

def home(request):
    username=request.session.get("username")
    password=request.session.get("password")

    context={
        "username":username,
        "password":password
    }
    return render(request,"home.html",context)

def delete(request):
    request.session.flush()
    return redirect('app:home')