from django.shortcuts import render
from django.views.generic import ListView
from .models import Recipe

# Create your views here.


class Index(ListView):
    model = Recipe
    template_name = "Recipes/index.html"
