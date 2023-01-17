from django.urls import path
from .views import PostList, PostDetail, PostDeleteView, PostUpdateView, PostCreateView


urlpatterns = [
    path('', PostList.as_view(), name='posts'),
    path('<int:pk>', PostDetail.as_view(), name='post'),
    path('delete/<int:pk>', PostDeleteView.as_view(), name='delete_post'),
    path('update/<int:pk>', PostUpdateView.as_view(), name='update_posts'),
    path('create/', PostCreateView.as_view(), name='create_post'),


]
