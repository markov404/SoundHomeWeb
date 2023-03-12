
from django.db import transaction
from django.apps import apps
from django.core.exceptions import ObjectDoesNotExist
from django.core.files import File
from django.core.files.uploadedfile import InMemoryUploadedFile

from users.models import SoundHomeUsers, SoundHomeUsersAdditionalInfo
from utils.abstractions.types.error_type import Error
from logging import getLogger

log = getLogger(__name__)

def get_user_email_by_pk(pk: int) -> str | bool:
    try:
        usr = SoundHomeUsers.objects.get(pk=pk)
        email = usr.email
    except Exception as E:
        log.warning(f'{E}')
        return Error(f'Queryset error - {E}', code=500)
    else:
        return email


def get_user_additional_info_by_pk(pk: int) -> dict | bool:
    try:
        data = SoundHomeUsersAdditionalInfo.objects.get(pk=pk)
        output = data.__dict__
    except Exception as E:
        log.warning(f'{E}')
        return Error(f'Queryset error - {E}', code=500)
    else:
        return output


def get_user_additional_active_status(pk: int) -> str | bool:
    try:
        try:
            usr = SoundHomeUsers.objects.get(pk=pk)
        except ObjectDoesNotExist as Excp:
            raise Excp

        usr, created = SoundHomeUsersAdditionalInfo.objects.get_or_create(pk=pk)
        active = usr.active
    except Exception as E:
        log.warning(f'{E}')
        return Error(f'Queryset error - {E}', code=500)
    else:
        return active


def add_user_ava_and_nickname(pk: int, ava: InMemoryUploadedFile, nickname: str) -> bool:
    try:
        try:
            usr = SoundHomeUsers.objects.get(pk=pk)
        except ObjectDoesNotExist as Excp:
            raise Excp

        with transaction.atomic():
            usr, created = SoundHomeUsersAdditionalInfo.objects.get_or_create(pk=pk)
            usr.image = File(ava.open(), name=f'{pk}_{ava.name}') 
            usr.nickname = nickname
            usr.save()
    except Exception as E:
        log.warning(f'{E}')
        return Error(f'Queryset error - {E}', code=500)
    else:
        return True


def change_user_active(pk: int, active: bool) -> bool:
    try:
        try:
            usr = SoundHomeUsers.objects.get(pk=pk)
        except ObjectDoesNotExist as Excp:
            raise Excp

        usr, created = SoundHomeUsersAdditionalInfo.objects.get_or_create(pk=pk)
        usr.active = active
        usr.save()
        output = usr
    except Exception as E:
        log.warning(f'{E}')
        return Error(f'Queryset error - {E}', code=500)
    else:
        return output


def add_user_ava_and_nickname_end_set_user_active(
    pk: int, 
    ava: InMemoryUploadedFile,
    nickname: str) -> bool | Error:
    try:
        try:
            usr = SoundHomeUsers.objects.get(pk=pk)
        except ObjectDoesNotExist as Excp:
            raise Excp

        with transaction.atomic():
            usr, created = SoundHomeUsersAdditionalInfo.objects.get_or_create(pk=pk)
            usr.image = File(ava.open(), name=f'{pk}_{ava.name}') 
            usr.nickname = nickname
            usr.active = True
            usr.save()
    except Exception as E:
        log.warning(f'{E}')
        return Error(f'Queryset error - {E}', code=500)
    else:
        return True


def get_user_additional_image_url(pk: int) -> str | bool:
    try:
        usr = SoundHomeUsersAdditionalInfo.objects.get(pk=pk)
        image_url = usr.image.url
    except Exception as E:
        log.warning(f'{E}')
        return Error(f'Queryset error - {E}', code=500)
    else:
        return image_url


def get_user_additional_nickname(pk: int) -> str | bool:
    try:
        usr = SoundHomeUsersAdditionalInfo.objects.get(pk=pk)
        nickname = usr.nickname
    except Exception as E:
        log.warning(f'{E}')
        return Error(f'Queryset error - {E}', code=500)
    else:
        return nickname


def update_user_additional_image(pk: int, ava: InMemoryUploadedFile) -> bool:
    try:
        usr = SoundHomeUsersAdditionalInfo.objects.get(pk=pk)
        usr.image = File(ava.open(), name=f'{pk}_{ava.name}') 
        usr.save()
    except Exception as E:
        log.warning(f'{E}')
        return Error(f'Queryset error - {E}', code=500)
    else:
        return True


def update_user_additional_nickname(pk: int, text: str) -> bool:
    try:
        usr = SoundHomeUsersAdditionalInfo.objects.get(pk=pk)
        usr.nickname = text
        usr.save()
    except Exception as E:
        log.warning(f'{E}')
        return Error(f'Queryset error - {E}', code=500)
    else:
        return True


def get_user_own_review_links(pk: int) -> list:
    try:
        usrv = apps.get_model('reviews', 'userreview')
        output = []
        qs = usrv.objects.filter(user=pk)
        for rvw in qs:
            output.append(rvw.image.url)
    except Exception as E:
        log.warning(f'{E}')
        return Error(f'Queryset error - {E}', code=500)

    return output


def get_user_own_review_ids(pk: int) -> list:
    try:
        usrv = apps.get_model('reviews', 'userreview')
        output = []
        qs = usrv.objects.filter(user=pk)
        for rvw in qs:
            output.append(rvw.id)
    except Exception as E:
        log.warning(f'{E}')
        return Error(f'Queryset error - {E}', code=500)

    return output

def get_user_own_review_album_title(pk: int) -> list:
    try:
        usrv = apps.get_model('reviews', 'userreview')
        output = []
        qs = usrv.objects.filter(user=pk)
        for rvw in qs:
            output.append(rvw.album_title)
    except Exception as E:
        log.warning(f'{E}')
        return Error(f'Queryset error - {E}', code=500)

    return output


def get_user_favourites_reviews(pk: int) -> list:
    try:
        likes_model = apps.get_model('users', 'SoundHomeUsersWhatUsersLikes')
        user_model = apps.get_model('users', 'SoundHomeUsers')
        usr = user_model.objects.get(pk=pk)
        qs = likes_model.objects.filter(user=usr)
        output = []
        for rv in qs:
            output.append(rv.user_review)
    except Exception as E:
        log.warning(f'{E}')
        return Error(f'Queryset error - {E}', code=500)
    
    return output


def get_user_favourites_reviews_images(pk: int) -> list:
    try:
        likes_model = apps.get_model('users', 'SoundHomeUsersWhatUsersLikes')
        user_model = apps.get_model('users', 'SoundHomeUsers')
        usr = user_model.objects.get(pk=pk)
        qs = likes_model.objects.filter(user=usr)
        output = []
        for rv in qs:
            output.append(rv.user_review.image.url)
    except Exception as E:
        log.warning(f'{E}')
        return Error(f'Queryset error - {E}', code=500)
    
    return output

def get_user_favourites_reviews_ids(pk: int) -> list:
    try:
        likes_model = apps.get_model('users', 'SoundHomeUsersWhatUsersLikes')
        user_model = apps.get_model('users', 'SoundHomeUsers')
        usr = user_model.objects.get(pk=pk)
        qs = likes_model.objects.filter(user=usr)
        output = []
        for rv in qs:
            output.append(rv.user_review.pk)
    except Exception as E:
        log.warning(f'{E}')
        return Error(f'Queryset error - {E}', code=500)
    
    return output
