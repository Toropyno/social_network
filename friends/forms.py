from django.forms import ModelForm

from friends.models import FriendshipRequest


class FriendshipRequestForm(ModelForm):
    class Meta:
        model = FriendshipRequest
        fields = ['from_user', 'to_user']