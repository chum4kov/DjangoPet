"""
URL configuration for todo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import include
from todoapp.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('add/', add, name='add_task'),
    path('update/<int:id_task>', update, name='update_task'),
    path('delete/<int:id_task>', delete, name='delete_task'),
    path('login/', UserLoginView.as_view(), name='login_user'),
    path('register/', UserRegisterView.as_view(), name='register_user'),
    path('logout/', logout_user, name='logout'),
    path('captcha/', include('captcha.urls'))
]
