
from reviews.services.interfaces.ICommand import ICommand
from utils.abstractions.abstract_classes.abs_services import BaseService
from reviews.components.database_requests import (
    get_latest_review_id, is_user_like_review, like_or_unlike_user_review)


class LatestReviewId(ICommand):

    def execute(self) -> int:
        return self._extract_latest_review_id()

    def _extract_latest_review_id(self) -> int | None:
        return get_latest_review_id()


class DoUserLikeReviewWithId(BaseService):

    def execute(self, _id: int, _rv_id: int) -> None:
        self._get_bool_user_likes_it_or_not(_id, _rv_id)

    def _get_bool_user_likes_it_or_not(self, _id: int, _rv_id: int) -> None:
        is_he_like_it = is_user_like_review(_id, _rv_id)
        if self.get_error(is_he_like_it):
            self.errors.append('Problem with getting likes data')
            return
        self._got_entities.append({'data': is_he_like_it})


class LikeOrUnlikeIt(BaseService):

    def execute(self, _id: int, _rv_id: int) -> None:
        self._like_or_unlike_it(_id, _rv_id)

    def _like_or_unlike_it(self, _id: int, _rv_id: int) -> None:
        result = like_or_unlike_user_review(_id, _rv_id)
        if self.get_error(result):
            self.errors.append('Problem with getting likes data')
            return
        return
