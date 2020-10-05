from django.contrib.auth.models import User
from django import forms
from first_app.models import ProfileInfo

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    
    class Meta():
        model=User
        fields=('username','email','password')
        

class ProfileInfoForm(forms.ModelForm):
    class Meta():
        model=ProfileInfo     
        fields=('portfolio_site','profile_pic')
        