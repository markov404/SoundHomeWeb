

from django.db import transaction
from django.core.files import File

from reviews.models import Review, ReviewAudio, ReviewTranslation

from reviews.services.interfaces.ICommand import ICommand
from reviews.components.pitchf_scruber_builder import PitchFScrubberBuilder
from reviews.components.translator import Translator
from reviews.components.speecher import Speecher


class UpdateReviewsInDBService(ICommand):

    def execute(self):
        new_data = self._scrub_new_data()
        new_data = self._change_data_structure(new_data)

        self._translate_reviews(new_data)
        self._make_audio_revs(new_data)

        self._update_database(new_data)

    def _scrub_new_data(self) -> list[dict]:
        scruber = PitchFScrubberBuilder().build()
        scruber.update_data()  
        data = scruber.get_actual_data()
        scruber.quit_driver()

        del scruber

        return data

    def _translate_reviews(self, data: list[dict]) -> None:
        trns = Translator()
        for point in data:
            text = point['record_data']['review_text']
            translated = trns.translate(text)
            point['translation'] = translated

        del trns
    
    def _make_audio_revs(self, data: list[dict]) -> None:
        spchr = Speecher()
        for point in data:
            text = point['translation']
            file = spchr.get_speech_file_object(text)
            point['audio_bytes'] = file

        del spchr

    def _update_database(self, data: list[dict]) -> None:
        
        try:
            active_reviews = Review.objects.all().filter(active=True)
            active_reviews.delete()
        except:
            pass

        for point in data:
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
            except:
                pass

    def _change_data_structure(self, data: list[dict]) -> list[dict]:
        new_data_structure = []

        for record in data:
            new_data_structure.append(
                {
                    'record_data': record, 
                    'translation': None,
                    'audio_bytes': None
                    })

        return new_data_structure