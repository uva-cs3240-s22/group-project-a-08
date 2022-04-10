from django.db import models
from django.core.validators import MinValueValidator
# Source: 
# https://engineertodeveloper.com/getting-started-with-django-forms-create-a-recipe-app/
# https://engineertodeveloper.com/getting-started-with-formsets-create-a-recipe-app/

INTEGER_CHOICES= [tuple([x,x]) for x in range(1,11)]

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=150)
    prep_time = models.IntegerField()
    cook_time = models.IntegerField()
    servings = models.IntegerField(choices=INTEGER_CHOICES)
    upload = models.ImageField(upload_to='media/', blank=True, default="static 'stock.jpg'")

    # meal type
    BREAKFAST = 'BR'
    LUNCH = 'LU'
    DINNER = 'DI'
    SNACK = 'SN'
    OTHER = 'OT'
    MEAL_TYPE_CHOICES = [
        (BREAKFAST, 'Breakfast'),
        (LUNCH, 'Lunch'),
        (DINNER, 'Dinner'),
        (SNACK, 'Snack'),
        (OTHER, 'Other'),
    ]
    meal_type = models.CharField(
        max_length=2,
        choices=MEAL_TYPE_CHOICES,
        default=OTHER,
    )

    # dietary restriction
    VEGETARIAN = 'VE'
    VEGAN = 'VG'
    GLUTENFREE = 'GF'
    NORESTRICTION = 'NR'
    DIET_CHOICES = [
        (VEGETARIAN, 'Vegetarian'),
        (VEGAN, 'Vegan'),
        (GLUTENFREE, 'Gluten-Free'),
        (NORESTRICTION, 'No Restriction')
    ]
    diet_restriction = models.CharField(
        max_length=2,
        choices=DIET_CHOICES,
        default=NORESTRICTION,
    )

    def __str__(self):
        return self.title

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.FloatField(validators=[MinValueValidator(0.0)])

    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="ingredients")

    def __str__(self):
        return self.name

class Step(models.Model):
    name = models.CharField(max_length=200)

    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="steps")

    def __str__(self):
        return self.name
