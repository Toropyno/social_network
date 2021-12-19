from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from rest_framework.decorators import action
from rest_framework.response import Response

from .. import services


class FriendshipRequestMixin:

    @action(detail=True, methods=['post'])
    def subscribe(self, request, pk=None):
        """
        Пописывает from_user на to_user
        """
        other_user = self.get_object()
        services.subscribe(from_user=request.user, to_user=other_user)
        if request.is_ajax():
            return Response()
        return redirect(request.META['HTTP_REFERER'])

    @action(detail=True, methods=['post'])
    def unsubscribe(self, request, pk=None):
        """
        Отписывает from_user от to_user
        """
        other_user = self.get_object()
        services.unsubscribe(from_user=request.user, to_user=other_user)
        if request.is_ajax():
            return Response()
        return redirect(request.META['HTTP_REFERER'])

    @action(detail=True, methods=['post'])
    def unfriend(self, request, pk=None):
        """
        Разрушает дружбу между пользователями
        """
        other_user = self.get_object()
        services.unfriend(request_user=request.user, user=other_user)
        return Response()

    @action(detail=True, methods=['post'])
    def accept_request(self, request, pk=None):
        """
        Принимает запрос на дружбу
        """
        other_user = self.get_object()
        services.accept_request(from_user=other_user, to_user=request.user)
        if request.is_ajax():
            return Response()
        return redirect(request.META['HTTP_REFERER'])
