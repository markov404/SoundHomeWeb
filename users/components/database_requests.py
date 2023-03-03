
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
        data, created = SoundHomeUsers.objects.get_or_create(pk=pk)
        output = data.__dict__
    except:
        output = None
    
    return output
