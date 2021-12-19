from django.contrib import admin

from photos.models import PhotoAlbum, Photo


@admin.register(PhotoAlbum)
class PhotoAlbumAdmin(admin.ModelAdmin):
    list_display = [
        '__str__',
        'id',
    ]


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass
