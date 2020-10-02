from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.shortcuts import redirect

from django.views.generic import ListView, CreateView
from django.views.generic.edit import FormView
# My forms/models
from .models import Recipe
from Comments.models import Comment
from .forms import CreateRecipeForm
from Comments.forms import CreateCommentForm

# Create your views here.


class Index(ListView):
    model = Recipe
    template_name = "Recipes/index.html"


class CreateRecipe(CreateView):
    form_class = CreateRecipeForm
    success_url = "/recipes/"
    template_name = "Recipes/create_recipe_form.html"
    
    def get_context_data(self, **kwargs):
        context = super(CreateRecipe, self).get_context_data()
        context["author"] = self.request.user
        return context
        
    def form_valid(self, form):
        form.author = self.get_context_data()["author"]
        form.save()
        return redirect('Recipes:CreateRecipe')


class ShowRecipe(FormView):
    template_name = "Recipes/show_recipe.html"
    form_class = CreateCommentForm
    success_url = '/recipes'

    def get_object(self):
        try:
            object = Recipe.objects.get(pk=self.kwargs['pk'])
        except ObjectDoesNotExist:
            raise Http404(f"Recipe {self.kwargs['pk']} doesn't exist")
        return object

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