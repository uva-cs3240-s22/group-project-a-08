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

urlpatterns = [
    path('admin/',      admin.site.urls),
    path("accounts/",   include("allauth.urls")),
    path('',            include("home.urls")),
    path('recipes/', include('recipes.urls')),
    path('review/', include('review.urls')),
    path('logout', LogoutView.as_view(), name='logout'),
]

# Allauth sources
# https://www.tutorialspoint.com/google-authentication-in-django
# https://www.section.io/engineering-education/django-google-oauth/