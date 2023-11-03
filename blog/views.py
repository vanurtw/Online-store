from django.shortcuts import render, get_object_or_404, redirect
from .models import Post


# Create your views here.


def blog(request):
    context = {}
    posts = Post.objects.all()
    context['posts'] = posts

    return render(request, 'blog/blog.html', context=context)


def post(request, post_id):
    post = Post.objects.filter(id__in=[post_id, post_id+1, post_id+2])
    context = {}
    context['post'] = post[0]
    context['posts'] = post[1:]
    return render(request, 'blog/singlepost.html', context=context)



