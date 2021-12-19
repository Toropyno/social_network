from .models import *


# Лайки
def add_like(post, user):
    """
    Лайкает post
    """
    like, created = Like.objects.get_or_create(post=post, user=user)
    return like


def remove_like(post, user):
    """
    Удаляет лайк с post
    """
    Like.objects.filter(post=post, user=user).delete()


def is_fan(post, user):
    """
    Проверяет, лайкал ли user post
    """
    if not user.is_authenticated:
        return False
    return Like.objects.filter(post=post, user=user).exists()


def get_fans(post):
    """
    Получает всех пользователей, которые лайкнули post
    """
    return User.objects.filter(like__post=post)


# Посты
def remove_post(post):
    """
    Удаляет post
    """
    post.delete()
