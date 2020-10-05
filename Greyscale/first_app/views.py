from django.shortcuts import render
from first_app.models import User
# Create your views here.

def index(request):
    return render(request,'first_app/index.html')

def login(request):
    return render(request,'first_app/login.html')

def user(request):
    usr_list=User.objects.order_by('first_name')
    usr_dict={'user':usr_list}
    return render(request,'first_app/user.html',context=usr_dict)
