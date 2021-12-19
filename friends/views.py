from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.views import View

from friends.forms import FriendshipRequestForm
from friends.models import FriendshipRequest
from friends.services import get_followers

User = get_user_model()


class FriendListView(View):
    template_name = 'friends/friend_list.html'

    def get(self, request, pk):
        context = self.get_context_data(request, pk)

        return render(request, self.template_name, context)

    def get_context_data(self, request, pk):
        page_owner = User.objects.get(pk=pk)  # владелец посещаемой страницы
        page_visitor = User.objects.get(pk=request.user.pk)  # посетитель страницы
        # если пользователь находится на собственной странице то page_owner = page_visitor
        is_my_page = (page_owner == page_visitor)
        context = {
            'page_owner': page_owner,
            'is_my_page': is_my_page,
            'friends': page_owner.friend_list.all().order_by('first_name', 'last_name'),
            'followers': get_followers(page_owner),
        }

        # context = {
        #     'common_friends': page_owner.friend_list.intersection(page_visitor.friend_list.all()),
        #
        # }
        return context
