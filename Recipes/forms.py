from django import forms
from .models import Recipe


class CreateRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'author', 'ingredients']


