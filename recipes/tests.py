from django.test import TestCase
from django.urls import reverse

from .models import Recipe

# Create your tests here.
class RecipeListViewTests(TestCase):
    def test_no_recipes(self):
    # If no questions exist
        response = self.client.get(reverse('recipes:all_recipes'))
        self.assertQuerysetEqual(response.context['recipe_list'], [])
    
    # def test_one_recipe(self):
    #     Recipe.objects.create(title="Cookies",intro="yummy cookies", prep_time=5, cook_time=10, servings=2)


# class RecipeSearchTests(TestCase):
#     def setUp(self):
#         Recipe.objects.create(title="Cookies",intro="yummy cookies", prep_time=5, cook_time=10, servings=2)
    
#     def test_search_success(self):
#         response = self.client.get("/recipes/search/?recipeTitle=a")
#         response = self.client.get(reverse('recipes:search'))
#         # self.assertQuerysetEqual(response.context['results_list'], [])
#         self.assertTrue(True)
        

