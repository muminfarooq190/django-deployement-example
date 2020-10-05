from django.contrib import admin
from django.urls import path,include
from first_app import views
app_name='first_app'
urlpatterns=[
    path('index/',views.index,name='index'),
    path('user_login/',views.user_login,name='user_login'),
    path('register/',views.register,name='register')
    
]