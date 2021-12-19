from django.shortcuts import redirect
from rest_framework import viewsets

from photos.api.mixins import AlbumMixin
from photos.api.serializers import AlbumSerializer


class AlbumViewSet(AlbumMixin, viewsets.ModelViewSet):
    serializer_class = AlbumSerializer

    def get_queryset(self):
        return self.request.user.photoalbum_set.all()

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        if request.is_ajax():
            return response
        return redirect(request.META['HTTP_REFERER'])
