from django.urls import path
from .views import PostList, PostDetail, PostDeleteView, PostUpdateView, PostCreateView, AuthPostListView, \
    ReplyDeleteView, confirmation

urlpatterns = [
    path('', PostList.as_view(), name='posts'),
    path('<int:pk>', PostDetail.as_view(), name='post'),
    path('delete/<int:pk>', PostDeleteView.as_view(), name='delete_post'),
    path('update/<int:pk>', PostUpdateView.as_view(), name='update_posts'),
    path('create/', PostCreateView.as_view(), name='create_post'),
    path('auth_page', AuthPostListView.as_view(), name='auth_posts'),
    path('delete_reply/<int:pk>', ReplyDeleteView.as_view(), name='delete_reply'),
    path('confirm_reply/<int:pk>', confirmation, name='confirm_reply'),
]
