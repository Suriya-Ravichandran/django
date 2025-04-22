from django.shortcuts import render ,redirect
# httpresponse use to send response 
from django.http import HttpResponse
# reverse url
from django.urls import reverse


# Create your views here.

# index page
def index(request):
    return HttpResponse("Hello World, Your at blogs Index")

# details page
def detail(request,post_id):
    return HttpResponse(f"You are viewing Post Details Page. And Id is: {post_id}")

# redirection

def old_url_redirect(request):
    return redirect(reverse('blog:new_page_url'))

def new_url_view(request):
    return HttpResponse("This is the new url")

