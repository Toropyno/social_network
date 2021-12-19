from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['get_full_name', 'username', 'id', 'sex']
    list_editable = ['sex']
    search_fields = ['first_name', 'last_name']
    filter_horizontal = ['friend_list']
