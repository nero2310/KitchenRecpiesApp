from django.urls import path
from Recipes.views import Index,CreateRecipe,ShowRecipe

from . import views

app_name = 'Recipes'

urlpatterns = [
    path('', Index.as_view(), name="index"),
    path('<int:pk>/',ShowRecipe.as_view(), name="ShowRecipe"),
    path('create',CreateRecipe.as_view(), name="CreateRecipe")
]
