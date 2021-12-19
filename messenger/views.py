from django.shortcuts import render, redirect
from django.views import View

from messenger.forms import MessageForm
from messenger.models import Chat
from messenger import services


class MessengerView(View):
    template_name = 'messenger/messenger.html'

    def get(self, request):
        context = self.get_context_data(request)
        return render(request, self.template_name, context)

    def get_context_data(self, request):
        context = {
            'title': 'Мессенджер',
            'chats': Chat.objects.filter(members=request.user, message__isnull=False),
        }
        return context


class ChatDetailView(View):
    template_name = 'messenger/chat_detail.html'

    def get(self, request, pk):
        chat = Chat.objects.get(pk=pk)
        context = {
            'messages': chat.message_set.all(),
            'chat': chat,
            'chat_client': services.get_chat_client(chat, request),
        }
        return render(request, self.template_name, context)


class MessageView(View):

    def post(self, request, pk):
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(request.META['HTTP_REFERER'])
