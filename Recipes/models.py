from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=200, blank=False)
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=200) # toDo If user aren't specify set user name to Anonymous
    ingredients =  ArrayField(models.CharField(max_length=100,blank=True))
