from django.shortcuts import render,redirect
from .models import Product
from .forms import ProductFrom
# Create your views here.

def productlist(request):
    products=Product.objects.all()
    context={
        "products":products
    }
    return render(request,"index.html",context)

def addproduct(request):
    form =ProductFrom(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('curd:productlist')
    
    context={
         "form":form
    }
    return render(request,"addproduct.html",context)
