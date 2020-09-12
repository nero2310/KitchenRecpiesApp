from django.urls import path
from  Recipes.views import Index

from . import views

urlpatterns = [
    path('', Index.as_view(), name="Index")
]
