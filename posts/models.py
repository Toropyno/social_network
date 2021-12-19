from django.db import models
from django.contrib.contenttypes.fields import GenericRelation

from main_app.models import User


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    text = models.TextField('Описание', max_length=2000)
    photo = models.ImageField('Прикрепить фото', upload_to='%Y/%m/', blank=True, null=True)
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
        ordering = ['-pub_date']

    def __str__(self):
        if self.author:
            return f'Запись {self.author.get_full_name()}'
        return f'Запись - {self.pk}'

    def get_comments(self):
        return self.comment_set.all()

    @property
    def total_likes(self):
        return self.like_set.count()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Запись')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    text = models.TextField('Текст комментария', max_length=2000)
    photo = models.ImageField('Прикрепить фото', upload_to='%Y/%m/', blank=True, null=True)
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['pub_date']

    def __str__(self):
        return f'{self.author.get_full_name()} - запись №{self.post_id}'


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Запись')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')

    class Meta:
        verbose_name = 'Лайк'
        verbose_name_plural = 'Лайки'

    def __str__(self):
        return f'{self.user.get_full_name()} - Запись №{self.post_id}'
