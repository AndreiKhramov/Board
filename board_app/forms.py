from django.forms import ModelForm
from .models import Post, Reply
from django import forms


class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes'
    )


# Создаём модельную форму
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'category', 'post_text']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'post_text': forms.Textarea(attrs={'class': 'form-control'}),
        }


class ReplyForm(ModelForm):
    class Meta:
        model = Reply
        fields = ['reply_text']

        widgets = {
            'reply_text': forms.Textarea(attrs={'class': 'form-control'})
        }
