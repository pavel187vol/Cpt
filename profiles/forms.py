from django import forms
from .models import Customer, Executer
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password')

class CustomerProfileInfoForm(forms.ModelForm):
     class Meta():
         model = Customer
         fields = ('first_name', 'last_name', 'email', 'phone')

class ExecuterProfileInfoForm(forms.ModelForm):
     class Meta():
         model = Executer
         fields = ('first_name', 'last_name', 'email', 'phone')
