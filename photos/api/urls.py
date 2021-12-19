from rest_framework.routers import DefaultRouter

from photos.api.viewsets import AlbumViewSet

router = DefaultRouter()
router.register(r'albums', AlbumViewSet, basename='album')
