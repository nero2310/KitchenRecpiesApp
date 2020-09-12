from django.shortcuts import render
from .models import Recipe

# Create your views here.


def index(request):
    query = Recipe.objects.get_queryset()
    return render(request, 'Recipes/index.html', context=query)
