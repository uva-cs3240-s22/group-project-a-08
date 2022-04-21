from django.db import models
from django.core.validators import MinValueValidator
# Source: 
# https://engineertodeveloper.com/getting-started-with-django-forms-create-a-recipe-app/
# https://engineertodeveloper.com/getting-started-with-formsets-create-a-recipe-app/

INTEGER_CHOICES= [tuple([x,x]) for x in range(1,11)]

# Create your models here.

class Recipe(models.Model):
    title = models.CharField(max_length=150, verbose_name = 'Recipe Title')
    prep_time = models.IntegerField(validators=[MinValueValidator(0)], verbose_name = 'Prep Time (mins)')
    cook_time = models.IntegerField(validators=[MinValueValidator(0)], verbose_name = 'Cook Time (mins)')
    servings = models.IntegerField(choices=INTEGER_CHOICES, validators=[MinValueValidator(0)])
    upload = models.ImageField(upload_to='media/', blank=True, default="static 'stock.jpg'", verbose_name = 'Picture')
    forkedid = models.IntegerField(default=0) # the parent recipe's pk
    isforked = models.IntegerField(default=0) # 0 if recipe is original, 1 if forked


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
        verbose_name="Meal Type"
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
        verbose_name = 'Dietary Restriction'
    )

    def __str__(self):
        return self.title

    def forked_recipes(self):
        return Recipe.objects.get_queryset().filter(isforked = 1, forkedid = self.id)

class Ingredient(models.Model):
    name = models.CharField(max_length=100, verbose_name = 'Ingredient')
    # quantity = models.FloatField(validators=[MinValueValidator(0.0)])
    quantity = models.CharField(max_length=100, default="", verbose_name = 'Quantity and Units')
    # units = models.CharField(max_length=100, default=" ")

    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="ingredients")

    def __str__(self):
        return self.name

class Step(models.Model):
    name = models.CharField(max_length=200, verbose_name = 'Step')

    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="steps")

    def __str__(self):
        return self.name