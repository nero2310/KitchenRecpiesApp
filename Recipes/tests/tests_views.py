from django.test import TestCase, RequestFactory
from ..models import Recipe

from ..views import ShowRecipe
from Comments.forms import CreateCommentForm


class ShowRecipeViewTest(TestCase):
    def setUp(self):
        self.recipe = Recipe.objects.create(name="pizza", times_visited=0, author="test",
                                            ingredients=["flour", "tests"]
                                            , prepare_dish_recipe="1.Prepare ingredients 2.Make my unit test working"
                                                                  "2.Make my unit test working")

    def test_comment_creation(self):  # Testing comment creation and created comment content
        request = RequestFactory().get("/")
        recipe = self.recipe
        view = ShowRecipe(request=request, kwargs={"pk": recipe.pk})
        form = CreateCommentForm(data={"recipe_id": recipe.pk, "author": "test", "content": "test_content"})
        comments = view.get_context_data()["comments"]
        assert (view.form_valid(form))
        self.assertEqual(first=[comment.content for comment in comments], second=["test_content"])
