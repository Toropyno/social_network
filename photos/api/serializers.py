from rest_framework import serializers

from ..models import PhotoAlbum, Photo


class AlbumSerializer(serializers.ModelSerializer):

    class Meta:
        model = PhotoAlbum
        fields = [
            'user',
            'title',
            'is_private',
        ]


class PhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Photo
        fields = [
            'album',
            'photo',
        ]
