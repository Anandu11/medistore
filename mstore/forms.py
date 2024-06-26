from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class Register(UserCreationForm):
    class Meta:
        model=User
        fields=['username',"first_name","last_name","email","password1","password2"]

class Loginform(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"username"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"password"}))

class orderform(forms.Form):
    address=forms.CharField(widget=forms.Textarea(attrs={"class":"form-control","placeholder":"address","row":5}))
