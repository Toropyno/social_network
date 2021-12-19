from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

User = get_user_model()


class PhotoAlbum(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    title = models.CharField('Название', max_length=150)
    is_private = models.BooleanField('Сделать приватным', default=False)

    class Meta:
        verbose_name = 'Фото-альбом'
        verbose_name_plural = 'Фото-альбомы'
        unique_together = ['user', 'title']

    def get_absolute_url(self):
        return reverse('photo_album-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.user.get_full_name()} - {self.title}'

    def get_cover(self):
        if self.photo_set.all():
            return self.photo_set.first().photo.url
        return 'http://127.0.0.1:8000/static/shop/images/img.png'


class Photo(models.Model):
    photo = models.ImageField('Фото', upload_to='%Y/%m/')
    album = models.ForeignKey(PhotoAlbum, on_delete=models.CASCADE, verbose_name='Альбом')
    desc = models.TextField('Описание', max_length=2000, blank=True)
    date_added = models.DateTimeField('Дата добавления', auto_now_add=True)

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = verbose_name
        ordering = ['date_added']
