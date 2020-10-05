from django.shortcuts import render
from first_app.forms import UserForm,ProfileInfoForm

from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required


def base(request):
    return render(request,'first_app/base.html')

def index(request):
    return render(request,'first_app/index.html')

@login_required
def special(request):
    username=request.user.username
    return render(request,'first_app/special.html',{'username':username})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('first_app:index')) 

def register(request):
    registered=False
    if request.method=='POST':
        user_form=UserForm(data=request.POST)
        profile_form=ProfileInfoForm(data=request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()
            
            profile=profile_form.save(commit=False)
            
            profile.user=user
            
            if 'profile_pic' in request.FILES:
                profile.profile_pic=request.FILES['profile_pic']
            profile.save()
            registered=True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form=UserForm()
        profile_form=ProfileInfoForm()
    return render(request,'first_app/register.html',{'user_form':user_form,
                                                     'profile_form':profile_form,
                                                     'registered':registered})                    



def user_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user=authenticate(username=username,password=password)
        print(user) 
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('first_app:index'))
            else:
               return HttpResponse('YOUR ACCOUNT IS DEACTIVATED')
        else:
           return HttpResponse('INAVLID CREDENTIALS SUPPLIED')
    else:
        return render(request,'first_app/login.html',{})        














