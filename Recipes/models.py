from django.db import models


# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=200, blank=False)
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=200) # toDo If user aren't specify set user name to Anonymous
    ingredients = models.JSONField(blank=False)
