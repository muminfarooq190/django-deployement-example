from django.urls import path
from first_app import views
urlpatterns=[
    path('',views.user,name='user'),
    path('login/',views.login,name='login')
]
