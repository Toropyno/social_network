from django.urls import path
from django.contrib.auth.decorators import login_required

from photos import views

urlpatterns = [
    path(
        'users/<int:user_pk>/photo_albums/',
        login_required(views.PhotoAlbumListView.as_view()),
        name='photo_album-list'
    ),
    path(
        'photo_albums/<int:pk>/',
        login_required(views.PhotoAlbumDetailView.as_view()),
        name='photo_album-detail'
    ),
]
