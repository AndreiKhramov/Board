from django.shortcuts import render
from django.views.generic import View, ListView, DetailView
from .models import Post, Reply, User


class PostList(ListView):
    model = Post
    ordering = 'add_time'
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 10


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'
