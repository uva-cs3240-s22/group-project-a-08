from django.db import models
from django.core.validators import MinValueValidator
# Source: 
# https://engineertodeveloper.com/getting-started-with-django-forms-create-a-recipe-app/
# https://engineertodeveloper.com/getting-started-with-formsets-create-a-recipe-app/

INTEGER_CHOICES= [tuple([x,x]) for x in range(1,11)]


# Recipe Managers
class RecipeFilterQuerySet(models.QuerySet):
    # meal type queries
    def breakfast(self):
        return self.filter(meal_type='BR')

    def lunch(self):
        return self.filter(meal_type='LU')

    def dinner(self):
        return self.filter(meal_type='DI')

    def snack(self):
        return self.filter(meal_type='SN')

    def other_mt(self):
        return self.filter(meal_type='OT')

    # difficulty queries

    # dietary queries

class FilterManager(models.Manager):
    def get_queryset(self):
        return RecipeFilterQuerySet(self.model, using=self._db)

    def breakfast(self):
        return self.get_queryset().breakfast()

    def lunch(self):
        return self.get_queryset().lunch()

    def dinner(self):
        return self.get_queryset().dinner()
        
    def snack(self):
        return self.get_queryset().snack()
    
    def other_mt(self):
        return self.get_queryset().other_mt()


# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=150)
    intro = models.TextField()
    prep_time = models.IntegerField()
    cook_time = models.IntegerField()
    servings = models.IntegerField(choices=INTEGER_CHOICES)
    objects = RecipeFilterQuerySet()

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

    def __str__(self):
        return self.title

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.FloatField(validators=[MinValueValidator(0.0)])

    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="ingredients")

    def __str__(self):
        return self.name
