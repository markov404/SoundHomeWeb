

from utils.abstractions.abstract_classes.abs_services import BaseService
from reviews.components.database_requests import create_user_review_and_get_it_pk


class CreateUserReviewService(BaseService):
    MANDATORY_FIELDS = {
        'score', 'image',
        'album_title', 'album_author',
        'review_title', 'review_text'
    }

    def execute(self, _id: int, data: dict):
        super().execute(data=data)

        review_id = self._make_user_review(data=data, _id=_id)
        if self.get_error(review_id):
            self.errors.append('Database error')
            return

        self._got_entities.append({'review_id': review_id})

    def _make_user_review(self, data: dict, _id: int) -> None:
        return create_user_review_and_get_it_pk(pk=_id, data=data)
