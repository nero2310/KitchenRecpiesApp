from django import forms
from .models import Recipe, Comment


# class CreateRecipe(forms.Form):
#     name = forms.CharField(max_length=200)
#     create_date = forms.DateTimeField()
#     modify_date = forms.DateTimeField()
#     author = forms.CharField(max_length=200) # toDo If user aren't specify set user name to Anonymous
#     ingredients = forms.JSONField()


class CreateRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'author', 'ingredients']


class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["recipe_id", "content", "author", "up_vote", "down_vote"]
        exclude = ("recipe_id",)

