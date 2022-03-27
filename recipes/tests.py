from django.test import TestCase
# need these next few lines if running tests in VSCode, https://www.youtube.com/watch?v=7RaPq2BnPCI
from django import setup
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
setup()

# Create your tests here.
# source: https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing

from .models import Recipe


class RecipeModelTests(TestCase):

    def setUp(self):
        # Setup run before every test method.
        pass

    def tearDown(self):
        # Clean up run after every test method.
        pass

    '''def test_submit_recipe(self):
        recipe = Recipe(title="Cookies",intro="yummy cookies", prep_time=5, cook_time=10, servings=2)'''

    def test_false_is_false(self):
        print("Method: test_false_is_false.")
        self.assertFalse(False)

    def test_false_is_true(self):
        print("Method: test_false_is_true.")
        self.assertTrue(False)

    def test_one_plus_one_equals_two(self):
        print("Method: test_one_plus_one_equals_two.")
        self.assertEqual(1 + 1, 2)
