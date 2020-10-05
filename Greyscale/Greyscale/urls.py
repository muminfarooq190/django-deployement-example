

from django.contrib import admin
from django.urls import path,include
from first_app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='home'),
    path('user/',include('first_app.urls'))
]
