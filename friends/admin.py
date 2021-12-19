from django.contrib import admin

from friends.models import FriendshipRequest


@admin.register(FriendshipRequest)
class FriendRequestAdmin(admin.ModelAdmin):
    pass
