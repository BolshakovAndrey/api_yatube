from rest_framework import viewsets

from api.serializers import PostSerializer, CommentSerializer
from posts.models import Post, Comment


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)


