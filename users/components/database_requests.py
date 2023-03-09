
from django.db import transaction
from django.core.files import File
from django.core.files.uploadedfile import InMemoryUploadedFile

from users.models import SoundHomeUsers, SoundHomeUsersAdditionalInfo
from logging import getLogger

log = getLogger(__name__)

def get_user_email_by_pk(pk: int) -> str | bool:
    try:
        usr = SoundHomeUsers.objects.get(pk=pk)
        email = usr.email
    except Exception as E:
        log.warning(f'{E}')
        return False
    else:
        return email


def get_user_additional_info_by_pk(pk: int) -> dict | bool:
    try:
        data = SoundHomeUsersAdditionalInfo.objects.get(pk=pk)
        output = data.__dict__
    except Exception as E:
        log.warning(f'{E}')
        return False
    else:
        return output


def get_user_additional_active_status(pk: int) -> dict | bool:
    try:
        usr, created = SoundHomeUsersAdditionalInfo.objects.get_or_create(pk=pk)
        active = usr.active
    except Exception as E:
        log.warning(f'{E}')
        return False
    else:
        return active


def add_user_ava_and_nickname(pk: int, ava: InMemoryUploadedFile, nickname: str) -> bool:
    try:
        with transaction.atomic():
            usr, created = SoundHomeUsersAdditionalInfo.objects.get_or_create(pk=pk)
            usr.image = File(ava.open(), name=f'{pk}_{ava.name}') 
            usr.nickname = nickname
            usr.save()
    except Exception as E:
        log.warning(f'{E}')
        return False
    else:
        return True


def change_user_active(pk: int, active: bool) -> bool:
    try:
        usr, created = SoundHomeUsersAdditionalInfo.objects.get_or_create(pk=pk)
        usr.active = active
        usr.save()
        output = usr
    except Exception as E:
        log.warning(f'{E}')
        return False
    else:
        return output


def add_user_ava_and_nickname_end_set_user_active(
    pk: int, 
    ava: InMemoryUploadedFile,
    nickname: str) -> bool:
    try:
        with transaction.atomic():
            usr, created = SoundHomeUsersAdditionalInfo.objects.get_or_create(pk=pk)
            usr.image = File(ava.open(), name=f'{pk}_{ava.name}') 
            usr.nickname = nickname
            usr.active = True
            usr.save()
    except Exception as E:
        log.warning(f'{E}')
        return False
    else:
        return True


def get_user_additional_image_url(pk: int) -> str | bool:
    try:
        usr = SoundHomeUsersAdditionalInfo.objects.get(pk=pk)
        image_url = usr.image.url
    except Exception as E:
        log.warning(f'{E}')
        return False
    else:
        return image_url


def get_user_additional_nickname(pk: int) -> str | bool:
    try:
        usr = SoundHomeUsersAdditionalInfo.objects.get(pk=pk)
        nickname = usr.nickname
    except Exception as E:
        log.warning(f'{E}')
        return False
    else:
        return nickname


def update_user_additional_image(pk: int, ava: InMemoryUploadedFile) -> bool:
    try:
        usr = SoundHomeUsersAdditionalInfo.objects.get(pk=pk)
        usr.image = File(ava.open(), name=f'{pk}_{ava.name}') 
        usr.save()
    except Exception as E:
        log.warning(f'{E}')
        return False
    else:
        return True


def update_user_additional_nickname(pk: int, text: str) -> bool:
    try:
        usr = SoundHomeUsersAdditionalInfo.objects.get(pk=pk)
        usr.nickname = text
        usr.save()
    except Exception as E:
        log.warning(f'{E}')
        return False
    else:
        return True
    
