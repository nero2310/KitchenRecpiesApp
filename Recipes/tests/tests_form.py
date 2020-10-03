from django.test import TestCase

from Recipes.forms import CreateRecipeForm


class RecipeFormTest(TestCase):
    def test_no_ingredients(self):
        form = CreateRecipeForm(
            data={"name": "pizza", "author": "nero", "prepare_dish_recipe": "test", "recipe_from": ""})
        self.assertEqual(form.errors, {'ingredients': ['This field is required.']})

    def test_no_data(self):
        form = CreateRecipeForm(data={})
        self.assertTrue(form.errors)  # Recipe form have to contain data

    def test_full_data(self):
        form = CreateRecipeForm(data={"author": "example", "name": "sample_food", "ingredients": "example ingredient"
            , "prepare_dish_recipe": "test", "recipe_from": "https://www.thekitchn.com/recipes"})
        self.assertFalse(form.errors)

    def test_no_user(self):
        form = CreateRecipeForm(data={"name": "ice cream", "ingredients": "ice", "prepare_dish_recipe": "Test example"})
        self.assertFalse(form.errors)
