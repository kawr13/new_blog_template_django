from django.shortcuts import render
from django.views import View
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
        commentform =
        posts = Post.published.get(id=post_id)
        context = {
            'title': 'Пост',
            'posts': posts,
        }
        return render(request, 'postapp/post.html', context=context)

