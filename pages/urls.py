from django.urls import path

from .views import HomePageView
from posts.views import PostListView, PostDetailView, PostCreateView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('posts/', PostListView.as_view(), name='posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/create/', PostCreateView.as_view(), name='post-create'),
]