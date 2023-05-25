from django.urls import path
from blog.views import UserPostListView, PostCreateView, PostDetailView


app_name = 'blog_urls'

urlpatterns = [
    path('posts/user/<str:username>/', UserPostListView.as_view(template_name='blog/user_posts.html'), name='user-posts-list'),
    path('post/create/', PostCreateView.as_view(template_name='blog/create_post.html'), name='create-post'),
    path('post/<slug:slug>/detail/', PostDetailView.as_view(template_name='blog/post_detail.html'), name='post-detail')
]

