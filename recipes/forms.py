from django import forms
from .models import Recipe, Ingredient, Step
from django.forms import DurationField, modelformset_factory # dynamic


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        exclude = ('recipe',)

class StepForm(forms.ModelForm):
    class Meta:
        model = Step
        exclude = ('recipe',)

IngredientFormSet = forms.inlineformset_factory(Recipe, Ingredient, form=IngredientForm, extra=0)
StepFormSet = forms.inlineformset_factory(Recipe, Step, form=StepForm, extra=0)
