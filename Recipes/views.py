from django.shortcuts import render
from django.views.generic import ListView,FormView
from .models import Recipe
from .forms import CreateRecipe
# Create your views here.


class Index(ListView):
    model = Recipe
    template_name = "Recipes/index.html"


class CreateRecipe(FormView):
    form_class = CreateRecipe
    template_name = "Recipes/create_recipe_form.html"