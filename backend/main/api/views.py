from rest_framework import viewsets

from main.models import Posts
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Posts.objects.all()

