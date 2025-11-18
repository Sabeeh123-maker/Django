"""
URL configuration for authentication project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Homeview.as_view(), name='home'),
    path('login/', views.Userlogin.as_view(), name='login'),
    path('register/', views.Registerview.as_view(), name='register'),
    path('logout/', views.Userlogout.as_view(), name='logout'),
    path('adm/', views.Adminhome.as_view(), name='adm'),
    path('teacher/', views.Teacherhome.as_view(), name='teacher'),
    path('student/', views.Studenthome.as_view(), name='student'),
]
