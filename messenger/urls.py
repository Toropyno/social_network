from django.urls import path
from django.contrib.auth.decorators import login_required

from messenger import views

urlpatterns = [
    path(
        'messenger/',
        login_required(views.MessengerView.as_view()),
        name='chat-list'
    ),
    path(
        'messenger/<int:pk>/',
        login_required(views.ChatDetailView.as_view()),
        name='chat-detail'
    ),
]
