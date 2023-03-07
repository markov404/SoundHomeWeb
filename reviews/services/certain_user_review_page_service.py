
from reviews.services.interfaces.ICommand import ICommand
from reviews.components.database_requests import (
    get_oldest_and_lates_pk_of_user_review,
    get_user_review_data_by_id,
    get_user_review_author_nickname_by_pk_of_review)

class CertainUserReviewPageService(ICommand):

    def execute(self, _id: int) -> dict:
        data = self._extract_user_review_data_by_id(_id)
        response = self._extract_oldest_and_lastest_pk_of_user_review()
        nickname = self._define_author_nickname(_id)
        print(nickname)

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
            'data': data, 'next_id': next_id, 'prev_id': prev_id, 'author_nickname': nickname}

    def _extract_user_review_data_by_id(self, _id) -> dict:
        return get_user_review_data_by_id(pk=_id)

    def _extract_oldest_and_lastest_pk_of_user_review(self) -> dict:
        return get_oldest_and_lates_pk_of_user_review()
    
    def _define_author_nickname(self, _id) -> str | None:
        return get_user_review_author_nickname_by_pk_of_review(pk=_id)