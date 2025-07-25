from django.shortcuts import render,redirect,get_object_or_404
from .models import Product
from .forms import ProductFrom
# Create your views here.

def productlist(request):
    title="Product List"
    products=Product.objects.all()
    context={
        "products":products,
        "title":title,
    }
    return render(request,"index.html",context)

def addproduct(request):
    title="Add Product"
    form =ProductFrom(request.POST or None,request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('curd:productlist')
    
    context={
         "form":form,
         "title":title
    }
    return render(request,"addproduct.html",context)

def updateproduct(request,pk):
    title="Update Product"
    product=get_object_or_404(Product,pk=pk)
    form = ProductFrom(request.POST or None, request.FILES or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('curd:productlist')
    return render(request,'addproduct.html',{"title":title,"form":form})

def deleteproduct(request,pk):
    product=get_object_or_404(Product,pk=pk)
    product.delete()
    return redirect('curd:productlist')
