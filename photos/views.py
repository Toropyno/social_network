from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.views import View

from photos.forms import PhotoForm, PhotoAlbumForm
from photos.models import PhotoAlbum

User = get_user_model()


class PhotoAlbumListView(View):
    template_name = 'photos/photo_album_list.html'

    def get(self, request, user_pk):
        context = self.get_context_data(request, user_pk)

        return render(request, self.template_name, context)

    def get_context_data(self, request, user_pk):
        page_owner = User.objects.get(pk=user_pk)
        page_visitor = request.user
        is_my_page = (page_owner == page_visitor)

        albums = page_owner.photoalbum_set.all()
        context = {
            'is_my_page': is_my_page,
            'page_owner': page_owner,
            'title': 'Фотографии',
            'albums': albums,
        }
        return context


class PhotoAlbumDetailView(View):
    template_name = 'photos/photo_album_detail.html'

    def get(self, request, pk):
        context = self.get_context_data(request, pk)
        return render(request, self.template_name, context)

    def get_context_data(self, request, pk):
        album = PhotoAlbum.objects.get(pk=pk)
        page_owner = album.user
        page_visitor = request.user
        is_my_page = (page_owner == page_visitor)
        context = {
            'is_my_page': is_my_page,
            'page_owner': page_owner,
            'title': 'Фотографии',
            'photos': album.photo_set.all(),
            'album': album,
            'form': PhotoForm,
        }
        return context
