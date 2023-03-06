
from django.db import transaction
from django.core.files import File
from django.core.files.uploadedfile import InMemoryUploadedFile

from users.models import SoundHomeUsers, SoundHomeUsersAdditionalInfo


def get_user_email_by_pk(pk: int) -> str | None:
    try:
        usr = SoundHomeUsers.objects.get(pk=pk)
        email = usr.email
    except:
        email = None
    
    return email


def get_user_additional_info_by_pk(pk: int) -> dict | None:
    try:
        data = SoundHomeUsersAdditionalInfo.objects.get(pk=pk)
        output = data.__dict__
    except:
        output = None
    
    return output


def get_user_additional_active_status(pk: int) -> dict | None:
    try:
        usr, created = SoundHomeUsersAdditionalInfo.objects.get_or_create(pk=pk)
        active = usr.active
    except:
        active = None
    
    return active


def add_user_ava_and_nickname(pk: int, ava: InMemoryUploadedFile, nickname: str) -> None:
    try:
        with transaction.atomic():
            usr, created = SoundHomeUsersAdditionalInfo.objects.get_or_create(pk=pk)
            usr.image = File(ava.open(), name=f'{pk}_{ava.name}') 
            usr.nickname = nickname
            usr.save()
    except:
        pass


def change_user_active(pk: int, active: bool) -> None:
    try:
        usr, created = SoundHomeUsersAdditionalInfo.objects.get_or_create(pk=pk)
        usr.active = active
        usr.save()
        output = usr
    except:
        output = None

    return output


def get_user_additional_image_url(pk: int) -> None:
    try:
        usr = SoundHomeUsersAdditionalInfo.objects.get(pk=pk)
        image_url = usr.image.url
    except:
        image_url = None
    
    return image_url


def get_user_additional_nickname(pk: int) -> None:
    try:
        usr = SoundHomeUsersAdditionalInfo.objects.get(pk=pk)
        nickname = usr.nickname
    except:
        nickname = None
    
    return nickname
