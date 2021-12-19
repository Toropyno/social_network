from rest_framework import viewsets, permissions

from .serializers import FriendshipRequestSerializer
from ..models import FriendshipRequest
from .mixins import FriendshipRequestMixin


class FriendshipRequestViewSet(viewsets.ModelViewSet):
    queryset = FriendshipRequest.objects.all()
    serializer_class = FriendshipRequestSerializer
    permission_classes = [permissions.IsAuthenticated]
