from django.contrib import admin

from posts.models import Comment, Like, Post


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    autocomplete_fields = ['author']
    list_display = ['__str__', 'id', 'author']
    ordering = ['author']


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    pass
