from django.shortcuts import redirect
from django.urls import reverse
from rest_framework.decorators import action
from rest_framework.response import Response

from photos.api.serializers import AlbumSerializer, PhotoSerializer


class AlbumMixin:

    @action(detail=True, methods=['post'])
    def change(self, request, pk=None):
        """
        Обновляет информацию об альбоме
        """
        print(request.data)
        album = self.get_object()
        serializer = AlbumSerializer(album, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
        if request.is_ajax():
            return Response(serializer.data)
        return redirect(request.META['HTTP_REFERER'])

    @action(detail=True, methods=['post'])
    def remove_album(self, request, pk=None):
        """
        Удаляет альбом
        """
        self.get_object().delete()
        if request.is_ajax():
            return Response()
        return redirect(reverse('photo_album-list', kwargs={'user_pk': request.user.pk}))

    @action(detail=True, methods=['post'])
    def add_photo(self, request, pk=None):
        """
        Добавляет фото в альбом
        """
        serializer = PhotoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        if request.is_ajax():
            return Response()
        return redirect(request.META['HTTP_REFERER'])
