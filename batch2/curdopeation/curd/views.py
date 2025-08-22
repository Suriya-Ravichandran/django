from django.shortcuts import render,redirect,get_object_or_404
from .models import Product,Category,User
from .forms import ProductFrom,SignupForm,SigninForm,ForgotPasswordForm,ResetPasswordForm
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import authenticate,login as signin,logout
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.template.loader import render_to_string
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


def login(request):
    form=SigninForm()
    if request.method== 'POST':
        form= SigninForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username,password=password)
            print(user)
            if user is not None:
                signin(request,user)
                return redirect("curd:productlist")
            print("login success")
    return render(request,'login.html',{"form":form})

def signup(request):
    form=SignupForm()
    if request.method == "POST":
        form=SignupForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False) #create user data
            user.set_password(form.cleaned_data["password"])
            user.save()
            messages.success(request,"Registration successfull")
    return render(request,'signup.html',{"form":form})


def signout(request):
    logout(request)
    return redirect("curd:login")

def forgot_password(request):
    form=ForgotPasswordForm()
    if request.method == 'POST':
        form=ForgotPasswordForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data['email']
            user=User.objects.get(email=email)
            token=default_token_generator.make_token(user)
            uid=urlsafe_base64_encode(force_bytes(user.pk))
            current_site=get_current_site(request)
            domain= current_site.domain
            subject="Reset Password Requested"
            message=render_to_string("reset_password_email.html",{
                "domain":domain,
                "uid":uid,
                "token":token
            })

            send_mail(subject,message,'info@gocosys.com',[email])
            messages.success(request,"Email has been sent")
    return render(request,'forgotpassword.html')

def resetpassword(request,uidb64,token):
     form=ResetPasswordForm()
     if request.method =='POST':
         form=ResetPasswordForm(request.POST)
         if form.is_valid():
             new_password =form.cleaned_data['password']
             try:
                uid=urlsafe_base64_decode(uidb64)
                user=User.objects.get(pk=uid)
             except(TypeError,ValueError,OverflowError,User.DoesNotExist):
                user=None
             if user is not None and default_token_generator.check_token(user,token):
                user.set_password(new_password)
                user.save()
                messages.success(request,"Your Password Has been Reset Successfully!")
                return redirect("curd:login")
             else:
                 messages.error(request,"The Password reset link is invaild")

     return render(request,'resetpassword.html',{"form":form})
