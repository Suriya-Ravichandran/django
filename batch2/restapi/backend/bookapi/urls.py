from django.urls import path
from . import views

app_name="bookapi"

urlpatterns=[
    path("",views.index,name="index"),
    path("api/books/",views.book_list,name="booklist"),
    path("api/createbook/",views.create_book,name="createbook"),
    path("api/getsinglebook/<int:pk>/",views.get_single_book,name="getsinglebook"),
    path("api/updatebook/<int:pk>/",views.update_book,name="updatebook"),
    path("api/deletebook/<int:pk>/",views.delete_book,name="deletebook"),
]
