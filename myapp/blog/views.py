from django.shortcuts import render ,redirect
# httpresponse use to send response 
from django.http import HttpResponse
# reverse url
from django.urls import reverse


# Create your views here.

# index page
def index(request):
    blog_title="Latest Post"
    return render(request,"blog/index.html",{'blog_title':blog_title})

# details page
def detail(request,post_id):
     return render(request,"blog/detail.html")

# redirection

def old_url_redirect(request):
    return redirect(reverse('blog:new_page_url'))

def new_url_view(request):
    return HttpResponse("This is the new url")

