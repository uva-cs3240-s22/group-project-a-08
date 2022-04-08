from django.shortcuts import redirect, render, get_object_or_404
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from recipes.models import Ingredient
from users.models import UserProfile
from .forms import IngredientFormSet, RecipeForm, StepFormSet
from .models import Recipe


class RecipeListView(generic.ListView):
    model = Recipe
    template_name = 'recipes/index.html'
    context_object_name = "recipe_list"

class RecipeDetailView(generic.DetailView):
    model = Recipe
    template_name = 'recipes/detail.html'

class SearchResultsView(generic.ListView):
    model = Recipe
    template_name = 'recipes/search_results.html'
    context_object_name = "results_list"

class SavedListView(generic.ListView):
    model = Recipe
    template_name = 'recipes/saved_recipes.html'
    context_object_name = "saved_list"

@login_required(login_url='/')
def create_recipe(request):
    if request.method == "GET":
        form = RecipeForm()
        formset = IngredientFormSet()
        step_formset = StepFormSet()
        return render(request, 'recipes/create_recipe.html', {"form":form, "formset":formset, "step_formset":step_formset})
    elif request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save()
            formset = IngredientFormSet(request.POST, instance=recipe)
            step_formset = StepFormSet(request.POST, instance=recipe)
            if formset.is_valid():
                formset.save()
            if step_formset.is_valid():
                step_formset.save()
            return redirect('/')
        else:
            return render(request, 'recipes/create_recipe.html', {"form":form})

@login_required(login_url='/')
def save_recipe(request, pk):
    user = UserProfile.objects.get(user = request.user)
    recipe = get_object_or_404(Recipe, id=pk)
    user.saved.add(recipe)
    return HttpResponseRedirect(reverse('recipes:detail', args=(pk,)))

@login_required(login_url='/')
def unsave_recipe(request, pk):
    user = UserProfile.objects.get(user = request.user)
    recipe = get_object_or_404(Recipe, id=pk)
    user.saved.remove(recipe)
    return HttpResponseRedirect(reverse('recipes:detail', args=(pk,)))

@login_required(login_url='/')
def search_recipes(request):
    if request.method == "GET":
        query = request.GET["recipeTitle"]
        results = Recipe.objects.filter(Q(title__icontains=query))
        result_dict = {"results": results}
    return render(request, "recipes/search_results.html", result_dict)

def filter_recipes(request):

    if request.method == "GET":
        query = request.GET.getlist('mealType')
        #print(query)
        results1 = Recipe.objects.all()
        results2 = Recipe.objects.all()
        # filtering by meal type
        if 'br' not in query:
            results1 = results1.exclude(Q(meal_type__iexact='BR'))
        if 'lu' not in query:
            results1 = results1.exclude(Q(meal_type__iexact='LU'))
        if 'di' not in query:
            results1 = results1.exclude(Q(meal_type__iexact='DI'))
        if 'sn' not in query:
            results1 = results1.exclude(Q(meal_type__iexact='SN'))
        if 'ot' not in query:
            results1 = results1.exclude(Q(meal_type__iexact='OT'))
        # filtering by dietary restriction
        if 've' not in query:
            results2 = results2.exclude(Q(diet_restriction__iexact='VE'))
        if 'vg' not in query:
            results2 = results2.exclude(Q(diet_restriction__iexact='VG'))
        if 'gf' not in query:
            results2 = results2.exclude(Q(diet_restriction__iexact='GF'))
        if 'nr' not in query:
            results2 = results2.exclude(Q(diet_restriction__iexact='NR'))

        # filling up queryset if empty
        if 'br' not in query and 'lu' not in query and 'di' not in query and 'sn' not in query and 'ot' not in query:
            results1 = Recipe.objects.all()
        if 've' not in query and 'vg' not in query and 'gf' not in query and 'nr' not in query:
            results2 = Recipe.objects.all()

        #print(results1)
        #print(results2)
        results = results1.intersection(results2)
        result_dict = {"results": results}
    return render(request, "recipes/filter_results.html", result_dict)



   