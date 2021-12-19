from rest_framework import serializers

from .. import services
from ..models import Post, User, Comment


class PostSerializer(serializers.ModelSerializer):
    is_fan = serializers.SerializerMethodField()
    url = serializers.HyperlinkedIdentityField(view_name='api:post-detail', read_only=True)

    class Meta:
        model = Post
        fields = [
            'url',
            'author',
            'text',
            'photo',
            'pub_date',
            'is_fan',
            'total_likes',
        ]

    def get_is_fan(self, obj):
        user = self.context.get('request').user
        return services.is_fan(obj, user)


class FanSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'username',
            'full_name',
        ]

    def get_full_name(self, obj):
        return obj.get_full_name()


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = [
            'post',
            'author',
            'text',
            'photo',
        ]
