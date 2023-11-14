from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from .forms import CommentsForms
from .models import *

# Create your views here.


class IndexView(View):
    def get(self, request):
        posts = Post.published.all()[:50]
        images = Gallery_images.objects.all().order_by('-created_at')[:10]
        context = {
            'title': 'Главная страница',
            'posts': posts,
            'images': images,
        }
        return render(request, 'postapp/index.html', context=context)


class PostView(View):
    def get(self, request, post_id):
        commentform = CommentsForms()
        posts = Post.published.get(id=post_id)
        comments = Comment.objects.filter(post=posts)
        context = {
            'title': 'Пост',
            'posts': posts,
            'form': commentform,
            'comments': comments,
        }
        return render(request, 'postapp/post.html', context=context)

    def post(self, request, post_id):
        commentform = CommentsForms(request.POST)
        if commentform.is_valid():
            comment = commentform.save(commit=False)
            comment.post = Post.published.get(id=post_id)
            comment.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

