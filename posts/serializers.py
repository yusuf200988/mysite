from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['user', 'image', 'pk', 'title', 'description', 'is_active', 'is_public']
        extra_kwargs = {
            'user': {'read_only':True}
        }