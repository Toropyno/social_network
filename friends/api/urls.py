from django.urls import path
from rest_framework.routers import DefaultRouter

from .viewsets import FriendshipRequestViewSet

# app_name = 'friends'
router = DefaultRouter()
router.register(r'friendship_requests', FriendshipRequestViewSet)

urlpatterns = [
]

# urlpatterns += router.urls
