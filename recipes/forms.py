from django import forms
from .models import Recipe, Ingredient, Step
from django.forms import DurationField, modelformset_factory # dynamic


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'
        exclude = ('isforked','forkedid')


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = '__all__'
        exclude = ('recipe',)

class StepForm(forms.ModelForm):
    class Meta:
        model = Step
        exclude = ('recipe',)

IngredientFormSet = forms.inlineformset_factory(Recipe, Ingredient, form=IngredientForm, extra=0, can_delete=False)
StepFormSet = forms.inlineformset_factory(Recipe, Step, form=StepForm, extra=0, can_delete=False)
