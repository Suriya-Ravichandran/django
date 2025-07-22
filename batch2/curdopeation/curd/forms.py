from django import forms
from .models import Product

class ProductFrom(forms.ModelForm):
    productname=forms.CharField(max_length=100,required=True)
    productprice=forms.CharField(max_length=100,required=True)
    productdist=forms.CharField(max_length=100,required=True)
    description=forms.CharField(required=True)

    class Meta:
        model = Product
        fields = ['productname', 'productprice', 'productdist','description']
