from django.test import TestCase
from django.urls import reverse

# Create your tests here.
# source: https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing

from .models import Recipe, Ingredient, Step
from users.models import UserProfile
from .forms import RecipeForm, IngredientForm



# Create your tests here.
class RecipeListTests(TestCase):
    
    def test_no_recipes(self):
        response = self.client.get(reverse('recipes:all_recipes'))
        self.assertQuerysetEqual(response.context['recipe_list'], [])
    
    def test_one_recipe(self):
        # recipe = Recipe.objects.create(title="Cookies", intro="yummy cookies", prep_time=5, cook_time=10, servings=2)
        recipe = Recipe.objects.create(title="Cookies", prep_time=5, cook_time=10, servings=2)
        response = self.client.get(reverse('recipes:all_recipes'))
        self.assertQuerysetEqual(response.context['recipe_list'], [recipe])


class RecipeSearchTests(TestCase):
    results = []

    def setUp(self):
        test_user1 = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        self.results.append(Recipe.objects.create(title="Cookies", prep_time=5, cook_time=10, servings=2, meal_type='SN', diet_restriction='NR'))
    
    def test_search_success(self):
        response = self.client.get("/recipes/search/?recipeTitle=Coo")
        self.assertContains(response, "Cookies")
    
    def test_search_failure(self):
        response = self.client.get("/recipes/search/?recipeTitle=fail")
        data = '<p>No recipes are available.</p>'
        self.assertInHTML(data,response.content.decode())
    
    def test_empty_query(self):
        response = self.client.get("/recipes/search/?recipeTitle=")
        self.assertContains(response, "Cookies")
        
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
        Recipe.objects.create(title="Cookies", prep_time=5, cook_time=10, servings=2)
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
        form = RecipeForm(data={'title':"Cookies", 'prep_time':5, 'cook_time':10, 'servings':2, 'meal_type':'SN', 'diet_restriction':'VE'})
        self.assertTrue(form.is_valid())

    def test_recipe_form_invalid(self):
        form = RecipeForm(data={'title':"", 'prep_time':5, 'cook_time':10, 'servings':2})
        self.assertFalse(form.is_valid())
    
class RecipeListViewTest(TestCase):

    def setUp(self):
        # Create two users
        test_user1 = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
        test_user2 = User.objects.create_user(username='testuser2', password='2HJ1vRV0Z&3iD')
        test_user1.save()
        test_user2.save()

        Recipe.objects.create(title="Cookies", prep_time=5, cook_time=10, servings=2)
        test_recipe = Recipe.objects.get(title="Cookies")
        Ingredient.objects.create(name='cookie dough', quantity=1.0, recipe = test_recipe)
        Ingredient.objects.create(name='chocolate', quantity=4.5, recipe = test_recipe)

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('recipes:create_recipe'))
        self.assertRedirects(response, '/?next=/recipes/create/')

class RecipeFilterTests(TestCase):

    def setUp(self):
        Recipe.objects.create(title="Cookies", prep_time=5, cook_time=10, servings=2, meal_type='SN', diet_restriction = 'NR')
        Recipe.objects.create(title="Vegetarian Pizza", prep_time=5, cook_time=10, servings=2, meal_type='DI', diet_restriction = 'VE')
        Recipe.objects.create(title="Gluten Free Cake", prep_time=5, cook_time=10, servings=2, meal_type='OT', diet_restriction = 'GF')
        Recipe.objects.create(title="Vegan Dinner", prep_time=5, cook_time=10, servings=2, meal_type='DI', diet_restriction = 'VG')
        test_recipe = Recipe.objects.get(title="Cookies")
    
    def test_no_recipes(self):
        response = self.client.get(reverse('recipes:filter')+'?mealType=lu&mealType=gf')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No recipes are available.")

    def test_recipes_available(self):
        response = self.client.get(reverse('recipes:filter')+'?mealType=di')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['results']), 2)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('recipes:filter'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Browse Recipes")
        
class RecipeDetailViewTests(TestCase):
    def test_recipe(self):
        recipe = Recipe.objects.create(title="Cookies", prep_time=5, cook_time=10, servings=2, meal_type='SN', diet_restriction='NR')
        url = reverse('recipes:detail', args=(recipe.id,))
        response = self.client.get(url)
        self.assertContains(response, recipe.title)

    def test_recipe_with_ingred(self):
        recipe = Recipe.objects.create(title="Cookies", prep_time=5, cook_time=10, servings=2, meal_type='SN', diet_restriction='NR')
        ingred = Ingredient.objects.create(name="dough", quantity="3 cups", recipe=recipe)
        url = reverse('recipes:detail', args=(recipe.id,))
        response = self.client.get(url)
        self.assertContains(response, ingred.name)

    def test_recipe_with_step(self):
        recipe = Recipe.objects.create(title="Cookies", prep_time=5, cook_time=10, servings=2, meal_type='SN', diet_restriction='NR')
        step = Step.objects.create(name="make cookies", recipe=recipe)
        url = reverse('recipes:detail', args=(recipe.id,))
        response = self.client.get(url)
        self.assertContains(response, step.name)
    

class SavedRecipeTests(TestCase):
    def setUp(self):
        test_user1 = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        #profile = UserProfile.objects.create(user=test_user1, )
        Recipe.objects.create(title="Cookies", prep_time=5, cook_time=10, servings=2)
        Recipe.objects.create(title="Pancakes", prep_time=10, cook_time=30, servings=4)
        # cookie = Recipe.objects.get(title = "Cookies")
        # print("id of " + str(cookie) + " is " + str(cookie.id))

    def test_save_recipe(self):
        save_response = self.client.get("/recipes/1/save")
        url = reverse('recipes:saved_recipes')
        page_response = self.client.get(url)
        self.assertContains(page_response, "Cookies")
    
    def test_not_saved_recipe(self):
        save_response = self.client.get("/recipes/1/save")
        url = reverse('recipes:saved_recipes')
        page_response = self.client.get(url)
        self.assertNotContains(page_response, "Pancakes")

    # def test_unsave_recipe(self):
    #     # print(Recipe.objects.filter(title="Cookies").exists())
    #     save_response = self.client.get("/recipes/1/save")
    #     save_response = self.client.get("/recipes/1/unsave")
    #     url = reverse('recipes:saved_recipes')
    #     page_response = self.client.get(url)
    #     self.assertNotContains(page_response, "Cookies")
    
    def test_no_saved_recipes(self):
        url = reverse('recipes:saved_recipes')
        page_response = self.client.get(url)
        self.assertContains(page_response, "No recipes saved yet")

# use assertEqual or assertNotEqual to see if the picture you chose matches or doesn't match the picture in the recipe
class RecipeImageTests(TestCase):
    def setUp(self):
        Recipe.objects.create(title="Cookies",  prep_time=5,    cook_time=10, servings=2, upload="cookie.png")
        Recipe.objects.create(title="Pancakes", prep_time=10,   cook_time=20, servings=4)

    def test_save_image(self):
        cookies  = Recipe.objects.get(title="Cookies")
        self.assertEqual(cookies.upload, "cookie.png")

    def test_no_save_image(self):
        recipe  = Recipe.objects.get(title="Pancakes")
        self.assertEqual(recipe.upload, "static 'stock.jpg'")

class ForkedRecipeTests(TestCase):

    def test_is_recipe_forked(self):
        cookies = Recipe.objects.create(title="Cookies", prep_time=5, cook_time=10, servings=2)
        cookies2 = Recipe.objects.create(title="Cookies Forked", prep_time=10, cook_time=30, servings=4, isforked = 1, forkedid = cookies.id)
        self.assertEqual(cookies2.isforked == 1, True)
        self.assertEqual(cookies2.forkedid == cookies.id, True)
    
    def test_recipe_appear_on_detail_page(self):
        cookies = Recipe.objects.create(title="Cookies", prep_time=5, cook_time=10, servings=2)
        cookies2 = Recipe.objects.create(title="Cookies Forked", prep_time=10, cook_time=30, servings=4, isforked = 1, forkedid = cookies.id)
        url = reverse('recipes:detail', args=(cookies.id,))
        page_response = self.client.get(url)
        self.assertContains(page_response, cookies2.title)

    def test_recipe_not_appear_on_detail_page(self):
        cookies = Recipe.objects.create(title="Cookies", prep_time=5, cook_time=10, servings=2)
        cookies2 = Recipe.objects.create(title="Cookies Forked", prep_time=10, cook_time=30, servings=4, isforked = 0, forkedid = 0)
        url = reverse('recipes:detail', args=(cookies.id,))
        page_response = self.client.get(url)
        self.assertNotContains(page_response, cookies2.title)
    
    def test_forked_recipe_back_button(self):
        cookies = Recipe.objects.create(title="Cookies", prep_time=5, cook_time=10, servings=2)
        cookies2 = Recipe.objects.create(title="Cookies Forked", prep_time=10, cook_time=30, servings=4, isforked = 1, forkedid = cookies.id)
        url = reverse('recipes:detail', args=(cookies2.id,))
        page_response = self.client.get(url)
        self.assertContains(page_response, "Back to parent recipe")

    def test_parent_recipe_back_button(self):
        cookies = Recipe.objects.create(title="Cookies", prep_time=5, cook_time=10, servings=2)
        cookies2 = Recipe.objects.create(title="Cookies Forked", prep_time=10, cook_time=30, servings=4, isforked = 1, forkedid = cookies.id)
        url = reverse('recipes:detail', args=(cookies.id,))
        page_response = self.client.get(url)
        self.assertContains(page_response, "Back to recipes index")
