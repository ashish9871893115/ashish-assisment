"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from venv import create
from django.contrib import admin
from django.urls import path
from api2 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name = 'homepage'),
    path('signup/', views.register, name='register'),
    path('login/', views.log_in, name = 'login'),
    path('logout/', views.log_out, name = 'logout'),
    path('viewbook/', views.viewbook_view),
    path('home/', views.homepage,),
    path('addbook/', views.addbook_view, name='addbook'),
    path('delete/<int:id>', views.delete),
    
    # path('viewbook/', views.viewbook_view,name='viewbook'),
    
    ]
