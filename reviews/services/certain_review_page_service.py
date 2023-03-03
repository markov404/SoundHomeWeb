
from reviews.services.interfaces.ICommand import ICommand
from reviews.models import Review, ReviewTranslation, ReviewAudio

class CertainReviewPageService(ICommand):

    def execute(self, id: int) -> dict:
        data = self._extract_review_data_by_id(id)        
        translation = self._extract_translation_data_by_id(id)
        audio_url = self._extract_audio_url_by_id(id)


        response = self._extract_oldest_and_lastest_pk_of_review()
        if response is not None:
            oldest = response['oldest']
            latest = response['latest']

            next_id = 0
            prev_id = 0
            if data['id'] == latest:
                next_id = oldest
                prev_id = data['id'] - 1
            elif data['id'] == oldest:
                next_id = data['id'] + 1
                prev_id = latest
            else:
                next_id = data['id'] + 1
                prev_id = data['id'] - 1
        else:
            next_id = None
            prev_id = None
            

        return {
            'data': data, 'translation': translation, 
            'next_id': next_id, 'prev_id': prev_id, 'audio_url': audio_url}

    def _extract_review_data_by_id(self, id: int) -> dict | None:
        try:
            record = Review.objects.get(pk=id)
        except:
            record = None
        
        return record.__dict__

    def _extract_translation_data_by_id(self, id: int) -> dict | None:
        try:
            record = ReviewTranslation.objects.get(pk=id)
            translation = record.translated_review_text
        except:
            translation = None
        
        return translation

    def _extract_audio_url_by_id(self, id: int) -> dict | None:
        try:
            record = ReviewAudio.objects.get(pk=id)
            audio_url = record.audio_review.url
        except:
            audio_url = None
        
        return audio_url

    def _extract_oldest_and_lastest_pk_of_review(self) -> dict | None:
        try:
            qs1 = Review.objects.all().filter(active=True)
            oldest = qs1[0].pk
            qs2 = Review.objects.all().filter(active=True).latest("pk")
            latest = qs2.pk

            output = {'oldest': oldest, 'latest': latest}
        except:
            output = None
        
        return output
