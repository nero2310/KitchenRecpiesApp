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

    def create_comment(self, view, data):
        form = CreateCommentForm(data=data)
        return view.form_valid(form)

    def test_comment_creation(self):  # Testing comment creation and created comment content
        request = RequestFactory().get("/")
        recipe = self.recipe
        view = ShowRecipe(request=request, kwargs={"pk": recipe.pk})
        form = CreateCommentForm(data={"recipe_id": recipe.pk, "author": "test", "content": "test_content"})
        comments = view.get_context_data()["comments"]
        assert (view.form_valid(form))
        self.assertEqual(first=[comment.content for comment in comments], second=["test_content"])

    def test_few_comments_creation(self):
        request = RequestFactory().get("/")
        recipe = self.recipe
        view = ShowRecipe(request=request, kwargs={"pk": recipe.pk})
        self.create_comment(view, data={"recipe_id": recipe.pk, "author": "test", "content": "test_content"})
        self.create_comment(view, data={"recipe_id": recipe.pk, "author": "test", "content": "wut"})  # Comment will
        self.create_comment(view, data={"recipe_id": recipe.pk, "author": "test", "content": "properly_comment"})
        # Comment will not be created because content is too short
        comments = view.get_context_data()["comments"]
        self.assertEqual(first=[comment.content for comment in comments], second=["test_content", "properly_comment"])
