from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=200, blank=False)
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=200)  # toDo If user aren't specify set user name to Anonymous
    ingredients = ArrayField(models.CharField(max_length=100, blank=True))


class Comment(models.Model):
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    content = models.TextField(max_length=1000, blank=False)
    author = models.CharField(max_length=200)
    create_date = models.DateTimeField(auto_now_add=True)
    up_vote = models.IntegerField(default=0)
    down_vote = models.IntegerField(default=0)
    
    class Meta:
        db_table = "Comments"

    def __str__(self):
        return self.content