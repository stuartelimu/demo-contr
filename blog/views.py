from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from .models import Post

def post_list(request):
    posts = Post.objects.all()[:20]
    data = {'results': list(posts.values('title', 'author__username', 'created_at'))}
    return JsonResponse(data)

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    data = {'results': {
        'title': post.title,
        'author': post.author.username,
        'created_at': post.created_at
    }}
    return JsonResponse(data)