# books/forms.py
from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    title=forms.CharField(label="title",max_length=255,required=True)
    author=forms.CharField(label="author",max_length=255,required=True)
    published_date=forms.DateField(label="published_date",required=True)

    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date']
