from django.test import TestCase
from django.urls import reverse

# Create your tests here.
# source: https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing

from .models import Recipe, Ingredient
from .forms import RecipeForm, IngredientForm


# Create your tests here.
class RecipeListTests(TestCase):
    def test_no_recipes(self):
    # If no questions exist
        response = self.client.get(reverse('recipes:all_recipes'))
        self.assertQuerysetEqual(response.context['recipe_list'], [])
    
    def test_one_recipe(self):
        recipe = Recipe.objects.create(title="Cookies",intro="yummy cookies", prep_time=5, cook_time=10, servings=2)
        response = self.client.get(reverse('recipes:all_recipes'))
        self.assertQuerysetEqual(response.context['recipe_list'], [recipe])


class RecipeSearchTests(TestCase):
    results = []

    def setUp(self):
        self.results.append(Recipe.objects.create(title="Cookies",intro="yummy cookies", prep_time=5, cook_time=10, servings=2))
    
    def test_search_success(self):
        response = self.client.get("/recipes/search/?recipeTitle=Coo")
        data = '<p class="card-text">Intro: yummy cookies <br>PrepTime: 5 <br>CookTime: 10 <br>Servings: 2 <br></p>'
        self.assertInHTML(data,response.content.decode())
    
    def test_search_failure(self):
        response = self.client.get("/recipes/search/?recipeTitle=fail")
        data = '<p>No recipes are available.</p>'
        self.assertInHTML(data,response.content.decode())
    
    def test_empty_query(self):
        response = self.client.get("/recipes/search/?recipeTitle=")
        data = '<p class="card-text">Intro: yummy cookies <br>PrepTime: 5 <br>CookTime: 10 <br>Servings: 2 <br></p>'
        self.assertInHTML(data,response.content.decode())
        


# create-form tests
# status: working
# need these next few lines if running tests in VSCode, https://www.youtube.com/watch?v=7RaPq2BnPCI

from django.contrib.auth.models import User
from django import setup
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
setup()

class RecipeIngredientModelTests(TestCase):

    def setUp(self):
        Recipe.objects.create(title="Cookies",intro="yummy cookies", prep_time=5, cook_time=10, servings=2)
        test_recipe = Recipe.objects.get(title="Cookies")
        Ingredient.objects.create(name='cookie dough', quantity=1.0, recipe = test_recipe)
        Ingredient.objects.create(name='chocolate', quantity=4.5, recipe = test_recipe)

    def tearDown(self):
        # Clean up run after every test method.
        pass

    
    def test_str_method_recipe(self):
        recipe = Recipe.objects.get(title="Cookies")
        self.assertEqual(str(recipe), recipe.title)

    def test_str_method_ingredient(self):
        ingred = Ingredient.objects.get(name="chocolate")
        self.assertEqual(str(ingred), ingred.name)

    def test_check_foreign_key(self):
        test_recipe = Recipe.objects.get(title="Cookies")
        ingred = Ingredient.objects.get(name="chocolate")
        self.assertEqual(test_recipe, ingred.recipe)

class FormTests(TestCase):

    def test_recipe_form_valid(self):
        form = RecipeForm(data={'title':"Cookies", 'intro':"yummy cookies", 'prep_time':5, 'cook_time':10, 'servings':2})
        self.assertTrue(form.is_valid())

    def test_recipe_form_invalid(self):
        form = RecipeForm(data={'title':"", 'intro':"yummy cookies", 'prep_time':5, 'cook_time':10, 'servings':2})
        self.assertFalse(form.is_valid())
    
class RecipeListViewTest(TestCase):

    def setUp(self):
        # Create two users
        test_user1 = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
        test_user2 = User.objects.create_user(username='testuser2', password='2HJ1vRV0Z&3iD')
        test_user1.save()
        test_user2.save()

        Recipe.objects.create(title="Cookies",intro="yummy cookies", prep_time=5, cook_time=10, servings=2)
        test_recipe = Recipe.objects.get(title="Cookies")
        Ingredient.objects.create(name='cookie dough', quantity=1.0, recipe = test_recipe)
        Ingredient.objects.create(name='chocolate', quantity=4.5, recipe = test_recipe)

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('recipes:create_recipe'))
        self.assertRedirects(response, '/?next=/recipes/create/')

    def test_logged_in_uses_correct_template(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('recipes:create_recipe'))

        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'testuser1')
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)

        # Check we used correct template
        self.assertTemplateUsed(response, 'recipes/create_recipe.html')
