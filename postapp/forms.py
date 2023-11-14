from django.forms import ModelForm

from postapp.models import Comment


class CommentsForms(ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']