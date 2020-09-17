from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from .models import Recipe
from .forms import CreateRecipeForm,CreateCommentForm


# Create your views here.


class Index(ListView):
    model = Recipe
    template_name = "Recipes/index.html"


class CreateRecipe(CreateView):
    form_class = CreateRecipeForm
    success_url = "/recipes/"
    template_name = "Recipes/create_recipe_form.html"


class ShowRecipe(DetailView):
    template_name = "Recipes/show_recipe.html"
    model = Recipe

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["recipe"] = Recipe.objects.filter(pk=self.kwargs["pk"])
        context["comments"] = Recipe.objects.filter(pk=self.kwargs["pk"])
        context["form"] = CreateCommentForm()
        return context
