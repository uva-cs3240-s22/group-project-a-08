from django.urls import path

from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.RecipeListView.as_view(), name='all_recipes'),
    path('<int:pk>/', views.RecipeDetailView.as_view(), name='detail'),
    path('create/', views.create_recipe, name='create_recipe'),
    path('search/', views.search_recipes, name='search'),
    path('filter/', views.filter_recipes, name='filter'),
]