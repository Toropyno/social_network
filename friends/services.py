from .models import *


def subscribe(from_user, to_user):
    """
    Пописывает from_user на to_user
    """
    request, created = FriendshipRequest.objects.get_or_create(from_user=from_user, to_user=to_user)
    return request


def unsubscribe(from_user, to_user):
    """
    Отписывает from_user от to_user
    """
    FriendshipRequest.objects.filter(from_user=from_user, to_user=to_user).delete()


def accept_request(from_user, to_user):
    """
    Принимает запрос на дружбу
    """
    request = FriendshipRequest.objects.filter(from_user=from_user, to_user=to_user)
    if request.exists():
        add_friend(from_user, to_user)
        request.delete()


def get_followers(user):
    """
    Получает подписчиков для user
    """
    qs = user.friendship_requests_received.all()
    return [x.from_user for x in qs]


def add_friend(user1, user2):
    """
    Делает пользователей друзьями
    """
    user1.friend_list.add(user2)


def unfriend(request_user, user):
    """
    Разрушает дружбу между пользователями
    """
    request_user.friend_list.remove(user)


def get_relationship_status(request_user, user):
    """
    Получает статус пользователя user по отношению к пользователю request_user
    """
    if are_friends(request_user, user):
        return 'Friend'
    elif is_follower(request_user, user):
        return 'Follower'
    elif is_following(request_user, user):
        return 'Following'
    return


def are_friends(user1, user2):
    """
    Проверяет, дружат ли пользователи
    """
    return user1 in user2.friend_list.all()


def is_follower(request_user, user):
    """
    Проверяет, является ли user подписчиком для request_user
    """
    return FriendshipRequest.objects.filter(from_user=user, to_user=request_user).exists()


def is_following(request_user, user):
    """
    Проверяет, является ли request_user подписчиком для user
    """
    return FriendshipRequest.objects.filter(from_user=request_user, to_user=user).exists()
