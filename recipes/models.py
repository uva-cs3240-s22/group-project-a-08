from django.db import models
from django.core.validators import MinValueValidator
# Source: 
# https://engineertodeveloper.com/getting-started-with-django-forms-create-a-recipe-app/
# https://engineertodeveloper.com/getting-started-with-formsets-create-a-recipe-app/

INTEGER_CHOICES= [tuple([x,x]) for x in range(1,11)]

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=150)
    intro = models.TextField()
    prep_time = models.DurationField()
    cook_time = models.DurationField()
    servings = models.IntegerField(choices=INTEGER_CHOICES)

    def __str__(self):
        return self.title

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.FloatField(validators=[MinValueValidator(0.0)])

    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="ingredients")

    def __str__(self):
        return self.name
