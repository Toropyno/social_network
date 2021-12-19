from rest_framework.routers import DefaultRouter

from .viewsets import UserViewSet
from posts.api.urls import router as posts_router
from friends.api.urls import router as friends_router
from messenger.api.urls import router as messenger_router
from photos.api.urls import router as photos_router

# app_name = 'users'
router = DefaultRouter()
router.register(r'users', UserViewSet)
router.registry.extend(posts_router.registry)
router.registry.extend(friends_router.registry)
router.registry.extend(messenger_router.registry)
router.registry.extend(photos_router.registry)

urlpatterns = [
]

urlpatterns += router.urls
