from rest_framework import serializers

from ..models import FriendshipRequest


class FriendshipRequestSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api:friendshiprequest-detail', read_only=True)

    class Meta:
        model = FriendshipRequest
        fields = [
            'url',
            'from_user',
            'to_user',
        ]
