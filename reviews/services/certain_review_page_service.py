
from utils.abstractions.abstract_classes.abs_services import BaseService
from reviews.components.database_requests import (
    get_review_data_by_id,
    get_translation_text_by_id,
    get_audio_url_by_id,
    get_list_of_pk_of_review)


class CertainReviewPageService(BaseService):

    def execute(self, _id: int) -> dict:
        self._extract_review_data_by_id(_id)
        self._extract_translation_data_by_id(_id)
        self._extract_audio_url_by_id(_id)
        self._extract_oldest_and_lastest_pk_of_review(_id)

    def _extract_review_data_by_id(self, id: int) -> dict | None:
        data = get_review_data_by_id(id)
        if self.get_error(data):
            self.errors.append('Problem with getting review data')
            return
        self._got_entities.append({'data': data})

    def _extract_translation_data_by_id(self, id: int) -> str | None:
        translation = get_translation_text_by_id(id)
        if self.get_error(translation):
            self.errors.append('Problem with getting translation data')
            return
        self._got_entities.append({'translation': translation})

    def _extract_audio_url_by_id(self, id: int) -> dict | None:
        audio_url = get_audio_url_by_id(id)
        if self.get_error(audio_url):
            self.errors.append('Problem with getting audio_url data')
            return
        self._got_entities.append({'audio_url': audio_url})

    def _extract_oldest_and_lastest_pk_of_review(
            self, _id: int) -> dict | None:
        list_of_ids = get_list_of_pk_of_review()
        if self.get_error(list_of_ids):
            self.errors.append('Problem with getting list of ids')
            return

        if list_of_ids is not None:

            next_id = 0
            prev_id = 0
            if _id == list_of_ids[-1]:
                next_id = list_of_ids[0]
                prev_id = list_of_ids[-2]
            elif _id == list_of_ids[0]:
                next_id = list_of_ids[1]
                prev_id = list_of_ids[-1]
            else:
                next_id = list_of_ids[list_of_ids.index(_id) + 1]
                prev_id = list_of_ids[list_of_ids.index(_id) - 1]
        else:
            next_id = None
            prev_id = None

        self._got_entities.append({'next_id': next_id, 'prev_id': prev_id})
