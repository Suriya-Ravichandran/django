from django.shortcuts import render,redirect,get_object_or_404
from .models import Product,Category
from .forms import ProductFrom
from django.core.paginator import Paginator
from django.db.models import Q
# Create your views here.

def productlist(request):
    title="Product List"
    query = request.GET.get('q', '')
    products=Product.objects.all().order_by('-create_at')

    if query:
        products = products.filter(
            Q(productname__icontains=query) |
            Q(description__icontains=query)
        )
     # pagenate
    pagenator=Paginator(products,10)
    print(pagenator)
    page_number=request.GET.get("page")
    page_object=pagenator.get_page(page_number)
    context={
        "products":products,
        "title":title,
        "page_obj":page_object,
        'query': query,
    }
    return render(request,"index.html",context)

def addproduct(request):
    title="Add Product"
    catagory=Category.objects.all()
    form =ProductFrom(request.POST or None,request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('curd:productlist')
    
    context={
         "form":form,
         "title":title,
         "catagory":catagory,
    }
    return render(request,"addproduct.html",context)

def updateproduct(request,slug):
    title="Update Product"
    product=get_object_or_404(Product,slug=slug)
    catagory=Category.objects.all()
    form = ProductFrom(request.POST or None, request.FILES or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('curd:productlist')
    return render(request,'addproduct.html',{"title":title,"form":form,"catagory":catagory,})

def deleteproduct(request,slug):
    product=get_object_or_404(Product,slug=slug)
    product.delete()
    return redirect('curd:productlist')
