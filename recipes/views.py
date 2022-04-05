from django.shortcuts import redirect, render
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from recipes.models import Ingredient
from .forms import IngredientFormSet, RecipeForm
from .models import Recipe


class RecipeListView(generic.ListView):
    model = Recipe
    template_name = 'recipes/index.html'
    context_object_name = "recipe_list"

class SearchResultsView(generic.ListView):
    model = Recipe
    template_name = 'recipes/search_results.html'
    context_object_name = "results_list"

@login_required(login_url='/')
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

def search_recipes(request):
    if request.method == "GET":
        query = request.GET["recipeTitle"]
        results = Recipe.objects.filter(Q(title__icontains=query))
        result_dict = {"results": results}
    return render(request, "recipes/search_results.html", result_dict)

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