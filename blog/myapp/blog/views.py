from django.shortcuts import render ,redirect
# httpresponse use to send response 
from django.http import HttpResponse
# reverse url
from django.urls import reverse

# logging
import logging

# getting data from post model
from .models import Post
from .models import AboutUs

from django.http import Http404

from django.core.paginator import Paginator

from .forms import ContactForm, LoginForm,RegisterForm

from django.contrib import messages
# Create your views here.

# static demo data
# posts=[
#         {"id":1,"title":"Post 1","content":"content of post 1"},
#         {"id":2,"title":"Post 2","content":"content of post 2"},
#         {"id":3,"title":"Post 3","content":"content of post 3"},
#         {"id":4,"title":"Post 4","content":"content of post 4"},
#     ]




# index page
def index(request):
    blog_title="Latest Post"
    all_posts=Post.objects.all()

    # pagenate
    pagenator=Paginator(all_posts,6)
    page_number=request.GET.get("page")
    page_object=pagenator.get_page(page_number)
    return render(request,"blog/index.html",{'blog_title':blog_title,"page_obj":page_object})

# details page
def detail(request,slug):
    try:
    # getting data from  model post id
        post=Post.objects.get(slug=slug)
        related_posts=Post.objects.filter(category=post.category).exclude(pk=post.id)
    except Post.DoesNotExist:
        raise Http404("Post Does Not Exist !")
    #  getting static data
    #  post=next((item for item in posts if item["id"] == int(post_id)),None)
    #  logger=logging.getLogger("testing")
    #  logger.debug(f"Post variable is {post}")
    return render(request,"blog/detail.html",{"post":post,"related_posts":related_posts})

# redirection

def old_url_redirect(request):
    return redirect(reverse('blog:new_page_url'))

def new_url_view(request):
    return HttpResponse("This is the new url")

def contact(request):
    if request.method == "POST":
        form=ContactForm(request.POST)
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        logger=logging.getLogger("testing")
        if form.is_valid():
            logger.debug(f"Form data is { form.cleaned_data["name"] } {form.cleaned_data["email"]} {form.cleaned_data["message"]}")
            success_message= "Your email has been sent !"
            return render(request,"blog/contact.html",{"form":form, "success_message":success_message})
        else:
            logger.debug(f"Form validation failure")
        return render(request,"blog/contact.html",{"form":form, "name":name,"email":email,"message":message})
    return render(request,"blog/contact.html")

def about(request):
    about_content = AboutUs.objects.first()
    if about_content is None or not about_content.content:
        about_content ="Default content goes Here"
    else:
        about_content =about_content.content
    return render(request,"blog/about.html",{"about_content":about_content})

def register(request):
    form =RegisterForm()
    if request.method == "POST":
        form =RegisterForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False) #create user data
            user.set_password(form.cleaned_data["password"])
            user.save()
            messages.success(request,"Registration successfull")
    return render(request,"blog/register.html",{"form":form})

def login(request):
    if request.method == "POST":
        form=LoginForm(request.POST)
        print("login success")
    return render(request,"blog/login.html",{"form":form})

