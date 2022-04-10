from django.contrib import admin
from .models import Recipe, Ingredient, Step

class IngredientInline(admin.TabularInline):
    model = Ingredient

class StepInline(admin.TabularInline):
    model = Step

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = [IngredientInline, StepInline,]