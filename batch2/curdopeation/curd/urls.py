from django.urls import path
from . import views

app_name="curd"

urlpatterns = [
    path("",views.login,name="login"),
    path("signup",views.signup,name="signup"),
    path("dashboard",views.productlist,name="productlist"),
    path("addproduct",views.addproduct,name="addproduct"),
    path("updateproduct/<str:slug>",views.updateproduct,name="updateproduct"),
    path("deleteproduct/<str:slug>",views.deleteproduct,name="deleteproduct"),
    path("logout",views.signout,name="signout"),
    path("forgotpassword",views.forgot_password,name="forgotpassword"),
    path("reset_password/<uidb64>/<token>",views.resetpassword,name="reset_password"),

]