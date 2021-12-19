from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class User(AbstractUser):
    MAN = 'M'
    WOMAN = 'W'
    SEX_CHOICES = [
        (MAN, 'Мужской'),
        (WOMAN, 'Женский'),
    ]

    photo = models.ImageField('Аватарка', upload_to='%Y/%m/', blank=True, null=True)
    birthday = models.DateField('День рождения', null=True, blank=True)
    sex = models.CharField('Пол', choices=SEX_CHOICES, null=True, blank=True, max_length=1)
    friend_list = models.ManyToManyField('self', verbose_name='Список друзей', blank=True)

    def get_absolute_url(self):
        return reverse('user', kwargs={'pk': self.pk})

    def get_avatar(self):
        if self.photo:
            return self.photo.url
        if not self.sex:
            return 'http://127.0.0.1:8000/static/main_app/images/img_6.png'
        if self.sex == 'M':
            return 'http://127.0.0.1:8000/static/main_app/images/img_2.png'
        if self.sex == 'W':
            return 'http://127.0.0.1:8000/static/main_app/images/img_3.png'

    def __str__(self):
        return self.get_full_name()

    def get_chat_url(self):
        pass
