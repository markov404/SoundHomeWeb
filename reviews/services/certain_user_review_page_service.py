
from utils.abstractions.abstract_classes.abs_services import BaseService
from reviews.components.database_requests import (
    get_oldest_and_lates_pk_of_user_review,
    get_user_review_data_by_id,
    get_user_review_author_nickname_by_pk_of_review,
    get_list_of_pk_of_user_review)

class CertainUserReviewPageService(BaseService):

    def execute(self, _id: int) -> dict:
        self._extract_user_review_data_by_id(_id)
        self._extract_oldest_and_lastest_pk_of_user_review(_id)
        self._define_author_nickname(_id)

    def _extract_user_review_data_by_id(self, _id: int) -> dict:
        data = get_user_review_data_by_id(pk=_id)
        if self.get_error(data):
            self.errors.append({'Problem with getting user review data'})
            return
        self._got_entities.append({'data': data})

    def _extract_oldest_and_lastest_pk_of_user_review(self, _id: int) -> dict:
        list_of_ids = get_list_of_pk_of_user_review()
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
                next_id = list_of_ids[list_of_ids.index(_id)+1]
                prev_id = list_of_ids[list_of_ids.index(_id)-1]
        else:
            next_id = None
            prev_id = None

        self._got_entities.append({'next_id': next_id, 'prev_id': prev_id})
    
    def _define_author_nickname(self, _id) -> str | None:
        author_nickname = get_user_review_author_nickname_by_pk_of_review(pk=_id)
        if self.get_error(author_nickname):
            self.errors.append('Problem with getting author nickname')
            return
        self._got_entities.append({'author_nickname': author_nickname})
