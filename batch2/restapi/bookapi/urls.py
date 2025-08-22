from django.urls import path
from . import views

app_name="bookapi"

urlpatterns=[
    path("",views.index,name="index"),
]
