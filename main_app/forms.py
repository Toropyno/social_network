from allauth.account.forms import SignupForm
from django.forms import ModelForm

from .models import *


class MyCustomSignupFrom(SignupForm):
    def save(self, request):
        user = super().save(request)
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.save()
        return user


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'birthday', 'sex']
