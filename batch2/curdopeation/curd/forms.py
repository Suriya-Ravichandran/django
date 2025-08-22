from django import forms
from .models import Product
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class ProductFrom(forms.ModelForm):
    productname=forms.CharField(max_length=100,required=True)
    productprice=forms.CharField(max_length=100,required=True)
    productdist=forms.CharField(max_length=100,required=True)
    description=forms.CharField(max_length=500,required=True)
    quantity = forms.CharField(max_length=100, required=True)
    class Meta:
        model = Product
        fields = ['productname', 'productprice', 'productdist','description','quantity', 'category','image']

class SignupForm(forms.ModelForm):
    username=forms.CharField(label="Username", max_length=100, required=True)
    email=forms.CharField(label="Email", max_length=100, required=True)
    password=forms.CharField(label="Password", max_length=100, required=True)
    password_confirm=forms.CharField(label="Confirm Password", max_length=100, required=True)
    
    class Meta:
        model = User
        fields= ["username","email","password"]

    def clean(self):
        cleaned_data= super().clean()
        password=cleaned_data.get("password")
        password_confirm=cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Password do not match")

class SigninForm(forms.Form):
    username=forms.CharField(label="Username", max_length=100, required=True)
    password=forms.CharField(label="Password", max_length=100, required=True)
    
    def clean(self):
        cleaned_data= super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        if username and password:
            user = authenticate(username=username,password=password)
            if user is None:
                raise forms.ValidationError("Invaild Email and Password")
            
class ForgotPasswordForm(forms.Form):
    email=forms.EmailField(label="email",max_length=254,required=True)

    def clean(self):
        cleaned_data=super().clean()
        email = cleaned_data.get('email')

        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError("No User Registered with this Email")
        

class ResetPasswordForm(forms.Form):
    password=forms.CharField(label="New Password",min_length=8)
    confirmpassword=forms.CharField(label="Confirm Password",min_length=8)
    
    def clean(self):
        cleaned_data=super().clean()
        password =cleaned_data.get("password")
        confirmpassword=cleaned_data.get("confirmpassword")

        if password and confirmpassword and password != confirmpassword:
            raise forms.ValidationError("Password Not Match")