from django.test import TestCase
from django.urls import reverse

from .models import UserProfile
from recipes.models import Recipe
from django.contrib.auth.models import User

from django import setup
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
setup()

class UserProfileModelTests(TestCase):
    
    def test_str_method(self):
        test_user1 = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
        profile = UserProfile.objects.get(user=test_user1)
        Recipe.objects.create(title="Cookies", prep_time=5, cook_time=10, servings=2)
        self.assertEqual(str(profile), test_user1.username)
