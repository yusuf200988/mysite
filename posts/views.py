from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.views.generic.edit import CreateView

from rest_framework.views import APIView

from .serializers import PostSerializer
from .models import Post


class PostListView(APIView):

    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return render(request, 'pages/post-list.html', context={'posts':serializer.data})


class PostDetailView(APIView):

    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        serializer = PostSerializer(post)
        username = get_user_model().objects.get(pk=serializer.data['user'])
        data = {'post':serializer.data, 'username':username}
        return render(request, 'pages/post-detail.html', context=data)
    
    
class PostCreateView(CreateView):
    model = Post
    template_name = 'posts/post-create.html'
    fields = ['title', 'description', 'user']