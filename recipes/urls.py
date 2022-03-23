from django.urls import path

from . import views

app_name = 'recipes'

urlpatterns = [
    path('create/', views.create_recipe, name='create_recipe'),
]