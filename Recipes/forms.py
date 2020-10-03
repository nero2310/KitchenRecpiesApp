from django import forms
from .models import Recipe


class CreateRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'author','recipe_from','ingredients','prepare_dish_recipe']
        exclude = ['author']


