from django.test import TestCase
from django import setup
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
setup()

# Create your tests here.

class SampleTests(TestCase):
    def test_true(self):
        self.assertTrue(True)