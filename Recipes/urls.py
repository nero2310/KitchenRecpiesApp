from django.urls import path
from  Recipes.views import Index,CreateRecipe

from . import views

urlpatterns = [
    path('', Index.as_view(), name="Index"),
    path('create',CreateRecipe.as_view(), name="CreateRecipe")
]
