from django.shortcuts import render
from django.views.generic import ListView,CreateView
from .models import Recipe
from .forms import CreateRecipeForm
# Create your views here.


class Index(ListView):
    model = Recipe
    template_name = "Recipes/index.html"


class CreateRecipe(CreateView):
    form_class = CreateRecipeForm
    success_url = "/recipes/"
    template_name = "Recipes/create_recipe_form.html"