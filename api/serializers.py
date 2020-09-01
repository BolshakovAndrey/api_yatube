from rest_framework import serializers
from posts.models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        fields = ('id', 'text', 'author', 'pub_date')
        model = Post

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        fileds = ('id','author', 'post', 'text', 'created')
        model = Comment
