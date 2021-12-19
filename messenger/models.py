import datetime

from django.db import models
from django.urls import reverse

from main_app.models import User


class Chat(models.Model):
    members = models.ManyToManyField(User, verbose_name='Участники')

    class Meta:
        verbose_name = 'Чат'
        verbose_name_plural = verbose_name + 'ы'

    def get_absolute_url(self):
        return reverse('chat-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.members.first().get_full_name()} - {self.members.last().get_full_name()}'

    @property
    def last_message(self):
        if self.message_set.exists():
            return self.message_set.latest('pub_date').text
        return

    @property
    def last_update(self):
        if self.message_set.exists():
            return self.message_set.latest('pub_date').pub_date
        return


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, verbose_name='Чат')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    text = models.TextField('Текст', max_length=5000)
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    is_checked = models.BooleanField('Прочитано', default=False)

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        ordering = ('pub_date',)

    def get_author(self):
        return self.author.first_name
