from django.shortcuts import redirect
from rest_framework import viewsets, permissions
from rest_framework.response import Response

from ..models import Post
from .serializers import PostSerializer
from .mixins import LikedMixin, PostMixin


class PostViewSet(PostMixin, LikedMixin, viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)

        if request.is_ajax():
            return response
        return redirect(request.META['HTTP_REFERER'])
