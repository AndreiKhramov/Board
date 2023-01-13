from django.db import models
from django.contrib.auth.models import User
from board_app.resorcies import PostTypes
from ckeditor.fields import RichTextField


class Post(models.Model):
    title = models.CharField(max_length=255)
    post_auth = models.ForeignKey(User, on_delete=models.CASCADE)
    add_time = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=2, choices=PostTypes)
    post_text = RichTextField(blank=True, null=True)

    # def __str__(self):
    #     return f'{self.title()}'


class Reply(models.Model):
    reply_text = models.TextField()
    reply_auth = models.ForeignKey(User, on_delete=models.CASCADE)
    reply_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    add_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.reply_text()} by {self.reply_auth()}'
