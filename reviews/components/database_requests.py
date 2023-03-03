
from django.db import transaction
from django.core.files import File
from reviews.models import Review, ReviewAudio, ReviewTranslation

def get_all_reviews_data_list() -> list[dict]:
    output = []
    try:
        records = Review.objects.all().filter(active=True)
        for record in records:
            output.append(record.__dict__)

        if len(output) == 0:
            output = None
    except:
        output = None
    
    return output


def get_review_data_by_id(pk: int) -> dict | None:
    try:
        record = Review.objects.get(pk=pk)
    except:
        record = None
    
    return record.__dict__


def get_translation_text_by_id(pk: int) -> str | None:
    try:
        record = ReviewTranslation.objects.get(pk=pk)
        translation = record.translated_review_text
    except:
        translation = None
    
    return translation


def get_audio_url_by_id(pk: int) -> str | None:
    try:
        record = ReviewAudio.objects.get(pk=pk)
        audio_url = record.audio_review.url
    except:
        audio_url = None
    
    return audio_url


def get_oldest_and_lates_pk_of_review() -> dict | None:
    try:
        qs1 = Review.objects.all().filter(active=True)
        oldest = qs1[0].pk
        qs2 = Review.objects.all().filter(active=True).latest("pk")
        latest = qs2.pk

        output = {'oldest': oldest, 'latest': latest}
    except:
        output = None
    
    return output


def get_latest_review_id() -> int | None:
    try:
        qs = Review.objects.all().filter(active=True)
        latest = qs.reverse()[0].pk
    except:
        latest = None

    return latest
    

def delete_all_active_review_objects() -> None:
    try:
        active_reviews = Review.objects.all().filter(active=True)
        active_reviews.delete()
    except:
        pass


def create_new_review_and_extends_records(point: dict) -> None:
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