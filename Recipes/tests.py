from django.test import TestCase

from .forms import CreateRecipeForm


class RecipeFormTest(TestCase):
    def test_no_ingredients(self):
        form = CreateRecipeForm(data={"name": "pizza", "author": "nero"})
        self.assertEqual(form.errors, {'ingredients': ['This field is required.']})
