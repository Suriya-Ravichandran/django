from . import views
from django.urls import path,include

app_name="curd"

urlpatterns = [
    path("",views.book_list,name="booklist"),
    path("addbook",views.book_add,name="addbook"),
    path("updatebook/<int:pk>",views.book_update,name="updatebook"),
    path("deletebook/<int:pk>",views.book_delete,name="deletebook"),
]