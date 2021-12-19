from django.forms import ModelForm

from photos.models import Photo, PhotoAlbum


class PhotoAlbumForm(ModelForm):
    class Meta:
        model = PhotoAlbum
        fields = ['user', 'title', 'is_private']


class PhotoForm(ModelForm):
    class Meta:
        model = Photo
        fields = ['photo', 'album', 'desc']
