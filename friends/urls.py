from django.contrib.auth.decorators import login_required
from django.urls import path

from friends import views

urlpatterns = [
    path(
        'friends/<int:pk>/',
        login_required(views.FriendListView.as_view()),
        name='friend-list'
    ),
]
