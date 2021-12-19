from rest_framework import viewsets, permissions
from django.contrib.auth import get_user_model

from friends.api.mixins import FriendshipRequestMixin
from messenger.api.mixins import ChatMixin
from .serializers import UserSerializer

User = get_user_model()


class UserViewSet(FriendshipRequestMixin, ChatMixin, viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
