import datetime
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from apistuff.models import StuffAndTokens
from utils.abstractions.types.error_type import Error
from logging import getLogger

log = getLogger(__name__)


def check_if_stuff_with_this_credentials_exists(username: str, password: str) -> int | Error | None:
    try:
        user = authenticate(username=username, password=password)
        if user is not None:
            return user.id
        else:
            return None

    except Exception as E:
        log.warning(f'{E}')
        return Error(f'{E}', code=500)


def update_stuff_token_by_stuff_id(_id: int, token: str):
    try:
        user = User.objects.get(id=_id)

        try:
            target_record = StuffAndTokens.objects.get(user=user)
            target_record.token = token
            target_record.duration_field = datetime.timedelta(hours=24)
        except StuffAndTokens.DoesNotExist:
            target_record = StuffAndTokens(
                user=user, token=token,
                duration_field=datetime.timedelta(hours=24))
            target_record.save()
        
    except Exception as E:
        log.warning(f'{E}')
        return Error(f'{E}', code=500)


def get_all_existing_tokens() -> list[str] | Error:
    try:
        records = StuffAndTokens.objects.all()
        output = []
        for record in records:
            output.append(record.token)
        
        return output
    except Exception as E:
        log.warning(f'{E}')
        return Error(f'{E}', code=500)
