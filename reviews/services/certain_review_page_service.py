
from reviews.services.interfaces.ICommand import ICommand

from reviews.components.database_requests import (
    get_review_data_by_id,
    get_translation_text_by_id,
    get_audio_url_by_id,
    get_oldest_and_lates_pk_of_review)

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
        return get_review_data_by_id(id)

    def _extract_translation_data_by_id(self, id: int) -> str | None:
        return get_translation_text_by_id(id)

    def _extract_audio_url_by_id(self, id: int) -> dict | None:
        return get_audio_url_by_id(id)

    def _extract_oldest_and_lastest_pk_of_review(self) -> dict | None:
        return get_oldest_and_lates_pk_of_review()
