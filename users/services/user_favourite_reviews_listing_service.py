

from utils.abstractions.abstract_classes.abs_services import BaseService
from users.components.database_requests import get_user_favourites_reviews


class UserFavouriteReviewsListingService(BaseService):

    def execute(self, _id: int) -> None:
        self._extract_user_favourite_rvws(_id)

    def _extract_user_favourite_rvws(self, _id: int) -> None:
        fav_revs = get_user_favourites_reviews(pk=_id)
        if self.get_error(fav_revs):
            self.errors.append('Problem with getting favoutire reviews')
            return
        self._got_entities.append({'fav_reviews': fav_revs})
