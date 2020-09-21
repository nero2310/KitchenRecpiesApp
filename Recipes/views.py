from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from .models import Recipe,Comment
from .forms import CreateRecipeForm,CreateCommentForm
from  django.shortcuts import redirect
from django.views.generic.edit import FormView

# Create your views here.


class Index(ListView):
    model = Recipe
    template_name = "Recipes/index.html"


class CreateRecipe(CreateView):
    form_class = CreateRecipeForm
    success_url = "/recipes/"
    template_name = "Recipes/create_recipe_form.html"


class ShowRecipe(FormView):
    template_name = "Recipes/show_recipe.html"
    form_class = CreateCommentForm
    success_url = '/recipes'

    def get_object(self):
        return Recipe.objects.filter(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["recipe"] = self.get_object()
        context["comments"] = Comment.objects.filter(recipe_id=self.kwargs["pk"])
        return context

    def form_valid(self, form):
        if form.is_valid():
            comment = form.save(commit=False)
            comment.recipe_id = self.get_object()
            comment.save()
        return super().form_valid(form)