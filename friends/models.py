from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

from main_app.models import User


class FriendshipRequest(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='От кого',
                                  related_name='friendship_requests_sent')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Кому',
                                related_name='friendship_requests_received')
    created = models.DateTimeField(default=timezone.now)
    accept = models.BooleanField('Принять запрос', default=False)

    class Meta:
        verbose_name = 'Запрос дружбы'
        verbose_name_plural = 'Запросы дружбы'
        unique_together = ['from_user', 'to_user']

    def __str__(self):
        return f'От {self.from_user.get_full_name()} к {self.to_user.get_full_name()}'
