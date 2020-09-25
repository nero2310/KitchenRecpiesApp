from django.db import models

# Create your models here.
from Recipes.models import Recipe


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
