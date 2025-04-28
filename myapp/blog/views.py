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
    posts=Post.objects.all()
    return render(request,"blog/index.html",{'blog_title':blog_title,"posts":posts})

# details page
def detail(request,post_id):
    try:
    # getting data from  model post id
        post=Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404("Post Does Not Exist !")
    #  getting static data
    #  post=next((item for item in posts if item["id"] == int(post_id)),None)
    #  logger=logging.getLogger("testing")
    #  logger.debug(f"Post variable is {post}")
    return render(request,"blog/detail.html",{"post":post})

# redirection

def old_url_redirect(request):
    return redirect(reverse('blog:new_page_url'))

def new_url_view(request):
    return HttpResponse("This is the new url")

