from django.urls import path
from django.contrib.auth.decorators import login_required

from main_app import views

urlpatterns = [
    path('', login_required(views.NewsFeedView.as_view()), name='news'),
    path('users/<int:pk>/', login_required(views.UserPageView.as_view()), name='user'),
    path('users/<int:pk>/update/', login_required(views.UserProfileUpdateView.as_view()), name='user_update'),
    path('search/', login_required(views.Search.as_view()), name='search'),
    ]
