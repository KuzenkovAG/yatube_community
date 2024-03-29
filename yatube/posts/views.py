from django.shortcuts import render, get_object_or_404
from .models import Post, Group

POST_LIMIT: int = 10


def index(request):
    """Main page"""
    template = 'posts/index.html'
    title = 'Последние обновления на сайте'
    posts = Post.objects.select_related('author', 'group')[:POST_LIMIT]
    context = {
        'title': title,
        'posts': posts
    }
    return render(request, template, context)


def group_post(request, slug):
    """Page of group"""

    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:POST_LIMIT]

    template = 'posts/group_list.html'
    title = f'Записи сообщества {group.title}'

    context = {
        'title': title,
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)
