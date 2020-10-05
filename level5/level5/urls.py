
from django.contrib import admin
from django.urls import path,include
from first_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('first__app/',include('first_app.urls')),
    path('',views.base,name='base'),
    path('logout/',views.user_logout,name='logout'),
    path('special/',views.special,name='special')
]
