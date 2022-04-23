from django.shortcuts import render
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from recipes.models import Recipe
from django.urls import reverse

# Create your views here.
@login_required(login_url='/')
def write_review(request, recipe):
    reviewedRecipe = Recipe.objects.get(id = recipe)
    if request.method == "GET":
        form = ReviewForm()
        return render(request, 'review/write_review.html', {"form":form})
    elif request.method == "POST":
        form = ReviewForm(request.POST, request.FILES)
        form.instance.author = request.user
        form.instance.recipe = reviewedRecipe
        if form.is_valid():
            review = form.save()
            reviewedRecipe.reviews.add(review)
            return HttpResponseRedirect(reverse('recipes:detail', args=(recipe,)))
            # return HttpResponseRedirect(reverse('recipes:detail', args=(recipe.id,)))
        else:
            return render(request, 'recipes/write_review.html', {"form":form})
