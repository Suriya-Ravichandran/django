from django.shortcuts import render ,redirect
# httpresponse use to send response 
from django.http import HttpResponse
# reverse url
from django.urls import reverse

# logging
import logging

# getting data from post model
from .models import Post

from django.http import Http404

from django.core.paginator import Paginator

from .forms import ContactForm

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

def contact_view(request):
    if request.method == "POST":
        form=ContactForm(request.POST)
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        logger=logging.getLogger("testing")
        if form.is_valid():
            logger.debug(f"Form data is { form.cleaned_data["name"] } {form.cleaned_data["email"]} {form.cleaned_data["message"]}")
        else:
            logger.debug(f"Form validation failure")
        return render(request,"blog/contact.html",{"form":form, "name":name,"email":email,"message":message})
    return render(request,"blog/contact.html")

