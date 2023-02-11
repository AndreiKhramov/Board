from django_filters import FilterSet
from .models import Post, Reply


class PostFilter(FilterSet):
    class Meta:
        model = Post
        fields = {'title': ['icontains'], 'category': ['icontains'], 'add_time': ['gt']}
