from django.shortcuts import redirect
from rest_framework.decorators import action
from rest_framework.response import Response

from .. import services
from .serializers import PostSerializer, CommentSerializer


class LikedMixin:

    @action(methods=['post'], detail=True)
    def like(self, request, pk=None):
        """
        Добавляет лайк к post
        """
        post = self.get_object()
        services.add_like(post, request.user)
        serializer = PostSerializer(post, context={'request': request})
        if request.is_ajax():
            return Response(serializer.data)
        return redirect(request.META['HTTP_REFERER'])


    @action(methods=['post'], detail=True)
    def unlike(self, request, pk=None):
        """
        Удаляет лайк с post
        """
        post = self.get_object()
        services.remove_like(post, request.user)
        serializer = PostSerializer(post, context={'request': request})
        if request.is_ajax():
            return Response(serializer.data)
        return redirect(request.META['HTTP_REFERER'])


class PostMixin:

    @action(methods=['post'], detail=True)
    def remove(self, request, pk=None):
        """
        Удаляет post
        """
        post = self.get_object()
        services.remove_post(post)
        if request.is_ajax():
            return Response()
        return redirect(request.META['HTTP_REFERER'])

    @action(methods=['post'], detail=True)
    def comment(self, request, pk=None):
        """
        Добавляет комментарий к записи
        """
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        if request.is_ajax():
            return Response()
        return redirect(request.META['HTTP_REFERER'])
