
from django.db import transaction
from django.core.files import File
from django.apps import apps

from reviews.models import Review, ReviewAudio, ReviewTranslation, UserReview
from utils.abstractions.types.error_type import Error
from logging import getLogger

log = getLogger(__name__)


def get_all_reviews_data_list() -> list[dict]:
    output = []
    try:
        records = Review.objects.all().filter(active=True)
        for record in records:
            output.append(record.__dict__)

        if len(output) == 0:
            output = None
    except Exception as E:
        log.warning(f'{E}')
        return Error(f'{E}', code=500)

    return output


def get_all_users_review_data_list() -> list[dict]:
    output = []
    try:
        records = UserReview.objects.all().filter(active=True)
        for record in records:
            data = record.__dict__
            data['image'] = record.image.url
            output.append(record.__dict__)

        if len(output) == 0:
            output = None
    except Exception as E:
        log.warning(f'{E}')
        return Error(f'{E}', code=500)

    return output


def get_review_data_by_id(pk: int) -> dict | None:
    try:
        record = Review.objects.get(pk=pk)
    except Exception as E:
        log.warning(f'{E}')
        return Error(f'{E}', code=500)

    return record.__dict__


def get_translation_text_by_id(pk: int) -> str | None:
    try:
        record = ReviewTranslation.objects.get(pk=pk)
        translation = record.translated_review_text
    except Exception as E:
        log.warning(f'{E}')
        return Error(f'{E}', code=500)

    return translation


def get_audio_url_by_id(pk: int) -> str | None:
    try:
        record = ReviewAudio.objects.get(pk=pk)
        audio_url = record.audio_review.url
    except Exception as E:
        log.warning(f'{E}')
        return Error(f'{E}', code=500)

    return audio_url


def get_oldest_and_lates_pk_of_review() -> dict | None:
    try:
        qs1 = Review.objects.all().filter(active=True)
        oldest = qs1[0].pk
        qs2 = Review.objects.all().filter(active=True).latest("pk")
        latest = qs2.pk

        output = {'oldest': oldest, 'latest': latest}
    except Exception as E:
        log.warning(f'{E}')
        return Error(f'{E}', code=500)

    return output


def get_list_of_pk_of_review() -> dict | None:
    try:
        qs1 = Review.objects.all().filter(active=True)
        output = []
        for rv in qs1:
            output.append(rv.pk)

    except Exception as E:
        log.warning(f'{E}')
        return Error(f'{E}', code=500)

    return output


def get_latest_review_id() -> int | None:
    try:
        qs = Review.objects.all().filter(active=True)
        latest = qs.reverse()[0].pk
    except Exception as E:
        log.warning(f'{E}')
        return Error(f'{E}', code=500)

    return latest


def delete_all_active_review_objects() -> None:
    try:
        active_reviews = Review.objects.all().filter(active=True)
        active_reviews.delete()
    except Exception as E:
        log.warning(f'{E}')
        return Error(f'{E}', code=500)

    return True


def create_new_review_and_extends_records(point: dict) -> None:
    try:
        with transaction.atomic():
            record = Review(**point['record_data'])
            record.active = True
            record.save()

            record_audio = ReviewAudio(
                review=record, name=f'{record.pk}_rev')
            record_audio.audio_review = File(
                point['audio_bytes'], name=f'{record.pk}_rev.mp3')
            record_audio.save()

            record_translation = ReviewTranslation(
                review=record, translated_review_text=point['translation'])
            record_translation.save()
    except Exception as E:
        log.warning(f'{E}')
        return Error(f'{E}', code=500)

    return True


def create_user_review_and_get_it_pk(pk, data) -> int | None:
    try:
        md = apps.get_model('users', 'SoundHomeUsers')
        with transaction.atomic():
            img = data['image']
            user = md.objects.get(pk=pk)

            rvw = UserReview(
                user=user,
                score=data['score'],
                image=File(img.open(), name=f'{pk}_{img.name}'),
                album_title=data['album_title'],
                album_author=data['album_author'],
                review_title=data['review_title'],
                review_text=data['review_text'],
                active=True)
            rvw.save()
            output = rvw.pk
    except Exception as E:
        log.warning(f'{E}')
        return Error(f'{E}', code=500)

    return output


def get_user_nickname_by_pk(pk: int) -> str | None:
    try:
        md = apps.get_model('users', 'SoundHomeUsers')
        user = md.objects.get(pk=pk)
        output = user.soundhomeusersadditionalinfo.nickname
    except Exception as E:
        log.warning(f'{E}')
        return Error(f'{E}', code=500)

    return output


def get_user_review_author_nickname_by_pk_of_review(pk: int) -> str | None:
    try:
        rvw = UserReview.objects.get(pk=pk)
        usr_id = rvw.user_id
        md = apps.get_model('users', 'SoundHomeUsers')
        user = md.objects.get(pk=usr_id)
        output = user.soundhomeusersadditionalinfo.nickname
    except Exception as E:
        log.warning(f'{E}')
        return Error(f'{E}', code=500)

    return output


def get_user_review_data_by_id(pk: int) -> dict | None:
    try:
        record = UserReview.objects.get(pk=pk)
        output = record.__dict__
        output['image'] = record.image.url
    except Exception as E:
        log.warning(f'{E}')
        return Error(f'{E}', code=500)

    return output


def get_oldest_and_lates_pk_of_user_review() -> dict | None:
    try:
        qs1 = UserReview.objects.all().filter(active=True)
        oldest = qs1[0].pk
        qs2 = UserReview.objects.all().filter(active=True).latest("pk")
        latest = qs2.pk

        output = {'oldest': oldest, 'latest': latest}
    except Exception as E:
        log.warning(f'{E}')
        return Error(f'{E}', code=500)

    return output


def get_list_of_pk_of_user_review() -> dict | None:
    try:
        qs1 = UserReview.objects.all().filter(active=True)
        output = []
        for rv in qs1:
            output.append(rv.pk)

    except Exception as E:
        log.warning(f'{E}')
        return Error(f'{E}', code=500)

    return output


def is_user_like_review(_user_id: iter, _rvw_id: int) -> Error | bool:
    try:
        usr_md = apps.get_model('users', 'SoundHomeUsersWhatUsersLikes')
        qs = usr_md.objects.filter(user=_user_id, user_review=_rvw_id)

        if len(qs) == 0:
            output = False
        elif len(qs) == 1:
            output = True
        else:
            raise Exception
    except Exception as E:
        log.warning(f'{E}')
        return Error(f'{E}', code=500)

    return output


def like_or_unlike_user_review(_user_id: iter, _rvw_id: int) -> Error | bool:
    try:
        usr_likes_md = apps.get_model('users', 'SoundHomeUsersWhatUsersLikes')
        usr_md = apps.get_model('users', 'SoundHomeUsers')
        rvw_md = apps.get_model('reviews', 'UserReview')
        qs = usr_likes_md.objects.filter(user=_user_id, user_review=_rvw_id)

        if len(qs) == 0:
            usr = usr_md.objects.get(pk=_user_id)
            rvw = rvw_md.objects.get(pk=_rvw_id)
            like_obj = usr_likes_md(user=usr, user_review=rvw)
            like_obj.save()
        elif len(qs) == 1:
            like_obj = qs[0]
            like_obj.delete()
        else:
            raise Exception
    except Exception as E:
        log.warning(f'{E}')
        return Error(f'{E}', code=500)

    return None
