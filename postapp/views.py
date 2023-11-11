from django.shortcuts import render
from django.views import View
from .models import *

# Create your views here.


class IndexView(View):
    def get(self, request):
        posts = Post.published.all()
        context = {
            'title': 'Главная страница',
            'posts': posts,
        }
        return render(request, 'postapp/index.html')