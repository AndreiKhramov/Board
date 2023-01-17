from django.shortcuts import render
from .models import Post, Reply, User
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .forms import PostForm


class PostList(ListView):
    model = Post
    ordering = '-add_time'
    template_name = 'posts.html'
    context_object_name = 'posts'
    form_class = PostForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PostForm()
        return context
    #
    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST)  # создаём новую форму, забиваем в неё данные из POST-запроса
    #
    #     if form.is_valid():  # если пользователь ввёл всё правильно и нигде не ошибся, то сохраняем новый пост
    #         form.save()
    #
    #     return super().get(request, *args, **kwargs)


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = 'create_post.html'
    form_class = PostForm
    success_url = '/'


class PostUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'create_post.html'
    form_class = PostForm
    success_url = '/'

# метод get_object мы используем вместо queryset, чтобы получить информацию об объекте, который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


# дженерик для удаления поста
class PostDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'delete_post.html'
    queryset = Post.objects.all()
    success_url = '/'
