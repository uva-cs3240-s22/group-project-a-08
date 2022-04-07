from django.db import models
from django.contrib.auth.models import User
from recipes.models import Recipe

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    saved = models.ManyToManyField(Recipe, related_name="saved_recipes", blank=True)

    def __str__(self):
        return str(self.user)
