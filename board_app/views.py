from django.shortcuts import render
from .models import Post, Reply, User
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .forms import PostForm, ReplyForm
from django.shortcuts import redirect
from .filters import PostFilter
from django.db.models.signals import post_save
# from .signals import notify_auth_confirm
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


class PostList(ListView):
    model = Post
    ordering = '-add_time'
    template_name = 'posts.html'
    context_object_name = 'posts'
    form_class = PostForm


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'
    form_class = ReplyForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ReplyForm()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)  # создаём новую форму, забиваем в неё данные из POST-запроса

        if form.is_valid():
            reply = form.save(commit=False)
            reply.reply_auth = request.user
            reply.reply_post_id = self.kwargs['pk']
            form.save()


    # def notify_auth_reply(self, instance, **kwargs):
            subject = f'User {reply.reply_auth} replies on {reply.reply_post}'
            auth_mail = reply.reply_post.post_auth.email
            send_mail(
                subject=subject,
                message=reply.reply_text,
                from_email='AndreySkillF2@yandex.ru',
                recipient_list=[str(auth_mail)]
            )

        return redirect('posts')
        # return HttpResponseRedirect(reverse('posts'))


class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = 'create_post.html'
    form_class = PostForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PostForm()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)  # создаём новую форму, забиваем в неё данные из POST-запроса
        if form.is_valid():
            post = form.save(commit=False)
            post.post_auth = request.user
            form.save()
        return redirect('posts')


class PostUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'create_post.html'
    form_class = PostForm
    success_url = '/'

# метод get_object мы используем вместо queryset, чтобы получить информацию об объекте, который мы собираемся редактировать
    def get_object(self, **kwargs):
        _id = self.kwargs.get('pk')
        return Post.objects.get(pk=_id)


# дженерик для удаления поста
class PostDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'delete_post.html'
    queryset = Post.objects.all()
    success_url = '/'


class AuthPostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'auth_page.html'
    context_object_name = 'auth_posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        context['post_list'] = Post.objects.filter(post_auth=self.request.user)
        # context['reply_list'] = Reply.objects.all()
        return context


class ReplyDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'delete_reply.html'
    queryset = Reply.objects.all()
    success_url = '/'


def confirmation(request, **kwargs):
    conf = Reply.objects.get(pk=kwargs['pk'])
    if not conf.confirmation:
        conf.confirmation = True
        conf.save()

    # def notify_auth_confirm(sender, instance, **kwargs):
        subject = f'User {conf.reply_post.post_auth} confirms your {conf.reply_text} on {conf.reply_post}'
        auth_mail = conf.reply_auth.email
        send_mail(
            subject='Confirmation',
            message=subject,
            from_email='AndreySkillF2@yandex.ru',
            recipient_list=[str(auth_mail)]
        )

    return redirect('auth_posts')

