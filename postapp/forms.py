from django.forms import ModelForm

class CommentsForms(ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']