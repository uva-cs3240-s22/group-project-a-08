from django.shortcuts import redirect, render
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q

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

from django.contrib.auth.decorators import login_required
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

# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'polls/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

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