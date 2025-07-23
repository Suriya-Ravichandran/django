from django.urls import path
from . import views

app_name="curd"

urlpatterns = [
    path("",views.productlist,name="productlist"),
    path("addproduct",views.addproduct,name="addproduct"),
    path("updateproduct/<int:pk>",views.updateproduct,name="updateproduct")

]