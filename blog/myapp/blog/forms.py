from django import forms
from django.contrib.auth.models import User
class ContactForm(forms.Form):
    name = forms.CharField(label="Name",max_length=100,required=True)
    email = forms.EmailField(label="Email",required=True)
    message=forms.CharField(label="Message",required=True)

class RegisterForm(forms.ModelForm):
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


class LoginForm(forms.Form):
    username=forms.CharField(label="username",max_length=100,required=True)
    password=forms.CharField(label="password",max_length=100,required=True)
    