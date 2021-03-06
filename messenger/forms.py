from django.forms import ModelForm

from messenger.models import Message


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['author', 'chat', 'text']