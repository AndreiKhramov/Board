from django.forms import ModelForm
from .models import Post
from django import forms


class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes'
    )


# Создаём модельную форму
class PostForm(ModelForm):
    # check_box = BooleanField(label='Алло, Галочка!')
    class Meta:
        model = Post
        fields = ['name', 'post_auth', 'category', 'text']
