from rest_framework import serializers
from django.contrib.auth import get_user_model

from friends import services as friends_services


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name='api:user-detail', read_only=True)
    full_name = serializers.CharField(source='get_full_name')
    friend_status = serializers.SerializerMethodField()
    photo = serializers.CharField(source='get_avatar')
    absolute_url = serializers.CharField(source='get_absolute_url')

    class Meta:
        model = User
        fields = [
            # 'url',
            'absolute_url',
            'id',
            'first_name',
            'last_name',
            'full_name',
            'friend_status',
            'photo',
        ]

    def get_friend_status(self, obj):
        request_user = self.context.get('request').user
        return friends_services.get_relationship_status(request_user, obj)


class WSUserSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source='get_full_name')
    photo = serializers.CharField(source='get_avatar')
    absolute_url = serializers.CharField(source='get_absolute_url')

    class Meta:
        model = User
        fields = [
            'absolute_url',
            'id',
            'first_name',
            'last_name',
            'full_name',
            'photo',
        ]
