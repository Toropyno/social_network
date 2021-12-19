from rest_framework.routers import DefaultRouter

from .viewsets import ChatViewSet

router = DefaultRouter()
router.register(r'chats', ChatViewSet, basename='chat')
