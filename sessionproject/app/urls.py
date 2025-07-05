from django.urls import path
from . import views
app_name="app"

urlpatterns=[
    path("",views.login,name="login"),
    path("home",views.home,name="home"),
    path("logout",views.delete,name="logout"),
]