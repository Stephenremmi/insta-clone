"""insta_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from insta import views
from django.contrib.auth import views as auth_views 
from django_registration.backends.one_step.views import RegistrationView 

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', include('insta.urls')),
    path(r'register/',views.register,name='register'),
    path(r'user_login/',views.user_login,name='user_login'),
    path(r'accounts/login/',views.user_login,name='user_login'),
    path(r'logout/', views.user_logout, name='user_logout'),
    path('accounts/register/',
        RegistrationView.as_view(success_url='/accounts/login/'),
        name='django_registration_register'),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    #url('accounts/', include('django_registration.backends.activation.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
