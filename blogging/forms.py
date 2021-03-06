from django.forms import ModelForm
from blogging.models import Post


class MyCommentForm(ModelForm):
    class Meta:
        model = Post
        exclude = ["published_date"]
