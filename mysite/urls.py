"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib.auth.views import LogoutView
from recipes.views import create_recipe

urlpatterns = [
    path('admin/',      admin.site.urls),
    path("accounts/",   include("allauth.urls")),
    path('',            include("home.urls")),
    path('recipes/create/', create_recipe, name="create_recipe") # url path subject to change
]

# Allauth sources
# https://www.tutorialspoint.com/google-authentication-in-django
# https://www.section.io/engineering-education/django-google-oauth/