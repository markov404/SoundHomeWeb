
from reviews.services.interfaces.ICommand import ICommand
from reviews.models import Review, ReviewTranslation

class CertainReviewPageService(ICommand):

    def execute(self, id: int) -> dict:
        response = self._extract_review_data_by_id(id)
        if response is not None:
            data: dict = response
        else:
            data = None
        
        response = self._exetract_translation_data_by_id(id)
        if response is not None:
            translation: str = response
        else:
            translation = None

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
            'next_id': next_id, 'prev_id': prev_id}

    def _extract_review_data_by_id(self, id: int) -> dict | None:
        try:
            record = Review.objects.get(pk=id)
        except:
            record = None
        
        return record.__dict__

    def _exetract_translation_data_by_id(self, id: int) -> dict | None:
        try:
            record = ReviewTranslation.objects.get(pk=id)
            translation = record.translated_review_text
        except:
            translation = None
        
        return translation

    def _extract_oldest_and_lastest_pk_of_review(self) -> dict | None:
        try:
            qs = Review.objects.all().filter(active=True)
            oldest = qs[0].pk
            latest = qs.reverse()[0].pk

            output = {'oldest': oldest, 'latest': latest}
        except:
            output = None
        
        return output
