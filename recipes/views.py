from django.shortcuts import redirect, render
from django.views import generic

from recipes.models import Ingredient
from .forms import IngredientFormSet, RecipeForm
from .models import Recipe


class RecipeListView(generic.ListView):
    model = Recipe
    template_name = 'recipes/index.html'
    context_object_name = "recipe_list"

def create_recipe(request):
    if request.method == "GET":
        form = RecipeForm()
        formset = IngredientFormSet()
        return render(request, 'recipes/create_recipe.html', {"form":form, "formset":formset})
    elif request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save()
            formset = IngredientFormSet(request.POST, instance=recipe)
            if formset.is_valid():
                formset.save()
            return redirect('/')
        else:
            return render(request, 'recipes/create_recipe.html', {"form":form})

'''
def create_recipe(request):
    template_name = 'create_recipe.html'
    if request.method == "GET":
        form = RecipeForm(request.GET or None)
        formset = IngredientFormSet(queryset=Ingredient.objects.none())
    elif request.method == "POST":
        form = RecipeForm(request.POST)
        formset = IngredientFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            recipe = form.save()
            for form in formset:
                ingredient = form.save(commit=False)
                ingredient.recipe = recipe.id
                ingredient.save()
            return redirect('/')
    return render(request, template_name, {
        "form":form,
        'formset':formset
    })
'''