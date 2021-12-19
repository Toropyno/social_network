from django.db.models import Q
from django.shortcuts import render
from django.views import View
from django.views.generic import UpdateView

from friends.models import FriendshipRequest
from messenger.services import get_chat
from photos.models import PhotoAlbum

from .forms import *


def has_friend_request(user1, user2):
    return FriendshipRequest.objects.filter(from_user__in=[user1, user2], to_user__in=[user1, user2]).exists()


def is_subscriber(page_visitor, page_owner):
    request = FriendshipRequest.objects.get(from_user__in=[page_visitor, page_owner],
                                            to_user__in=[page_visitor, page_owner])
    return request.to_user == page_visitor


def get_photo_count(user):
    albums = PhotoAlbum.objects.filter(user=user)
    counter = 0
    if albums:
        for album in albums:
            counter += album.photo_set.count()
    return counter


class UserPageView(View):
    template_name = 'main_app/user_page.html'
    login_url = 'account_login'

    def get(self, request, pk):
        context = self.get_context_data(request, pk)

        return render(request, self.template_name, context=context)

    def get_context_data(self, request, pk):
        page_owner = User.objects.get(pk=pk)  # владелец посещаемой страницы
        page_visitor = request.user  # посетитель страницы
        # если пользователь находится на собственной странице то page_owner = page_visitor
        is_my_page = (page_owner == page_visitor)
        context = {
            'title': page_owner.get_full_name(),
            'block_title': 'Записи',
            'page_owner': page_owner,
            'photos_count': get_photo_count(page_owner),
            'random_friends': page_owner.friend_list.order_by('?')[:6],
            'posts': page_owner.post_set.all(),
        }
        if is_my_page:
            context['is_my_page'] = is_my_page
            return context

        is_friend = page_visitor in page_owner.friend_list.all()
        context['is_friend'] = is_friend
        context['chat'] = get_chat(page_visitor, page_owner)

        if not is_friend:
            context['has_friend_request'] = has_friend_request(page_visitor, page_owner)
            if has_friend_request(page_visitor, page_owner):
                context['friend_request'] = FriendshipRequest.objects.get(to_user__in=[page_visitor, page_owner],
                                                                          from_user__in=[page_visitor, page_owner])
                context['is_subscriber'] = is_subscriber(page_visitor, page_owner)

        return context


class UserProfileUpdateView(UpdateView):
    model = User
    form_class = UserForm
    template_name = 'main_app/user_profile_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class Search(View):
    template_name = 'main_app/search_detail.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(request)
        return render(request, self.template_name, context=context)

    def get_context_data(self, request):
        q = request.GET.get('q')
        result = User.objects.filter(Q(first_name__icontains=q) | Q(last_name__icontains=q))
        context = {
            'q': q,
            'title': 'Поиск',
            'result': result,
        }

        return context


class NewsFeedView(View):
    template_name = 'main_app/news.html'
    login_url = 'account_login'

    def get(self, request):
        context = self.get_context_data(request)
        return render(request, self.template_name, context)

    def get_context_data(self, request):
        context = {
            'title': 'Новости',
            'block_title': 'Новости',
            'posts': self.get_news(request.user),
        }
        return context

    @staticmethod
    def get_news(user):
        friends = user.friend_list.all()
        if friends:
            news = friends[0].post_set.all().union(*[friend.post_set.all() for friend in friends]).order_by('-pub_date')
            return news
        return
