from django import forms
from .models import Recipe, Ingredient
from django.forms import DurationField, modelformset_factory # dynamic


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        exclude = ('recipe',)

IngredientFormSet = forms.inlineformset_factory(Recipe, Ingredient, form=IngredientForm)



'''
IngredientFormSet = modelformset_factory(
    Ingredient,
    fields=('name', 'quantity', ),
    extra=3,
    widgets={
        'name': forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Ingredient Name here'
            }
        ),
        'quantity': forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Quantity here'
            }
        )
    }
)
'''