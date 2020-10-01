from django.test import TestCase

from .forms import CreateRecipeForm


class RecipeFormTest(TestCase):
    def test_no_ingredients(self):
        form = CreateRecipeForm(data={"name": "pizza", "author": "nero"})
        self.assertEqual(form.errors, {'ingredients': ['This field is required.']})

    def test_no_data(self):
        form = CreateRecipeForm(data={})
        self.assertTrue(form.errors)  # Recipe form have to contain data

    def test_full_data(self):
        form = CreateRecipeForm(data={"author": "example", "name": "sample_food", "ingredients": "example ingredient"})
        self.assertFalse(form.errors)
    
    def test_no_user(self):
        form = CreateRecipeForm(data={"name":"ice cream","ingredients":"ice"})
        self.assertFalse(form.errors)
