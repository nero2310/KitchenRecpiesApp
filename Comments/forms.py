from django import forms

from Comments.models import Comment


class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["recipe_id", "content", "author", "up_vote", "down_vote"]
        exclude = ("recipe_id","up_vote","down_vote","author")