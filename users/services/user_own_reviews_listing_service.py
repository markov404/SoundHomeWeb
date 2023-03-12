
from utils.abstractions.abstract_classes.abs_services import BaseService
from users.components.database_requests import (
    get_user_own_review_ids, get_user_own_review_links, 
    get_user_own_review_album_title)


class UserOwnReviewsListingService(BaseService):

    def execute(self, _id: int):
        self._get_all_users_review_images_and_ids_data(_id)

    def _get_all_users_review_images_and_ids_data(self, _id: int):
        images = self._get_all_users_review_image_paths(_id)
        ids = self._get_all_users_review_id(_id)
        titles = self._get_all_users_review_album_title(_id)

        output = []
        for img, i, t in zip(images, ids, titles):
            output.append({'image': img, 'id': i, 'title': t})
        self._got_entities.append({'own_rvws': output})
    
    def _get_all_users_review_image_paths(self, _id: int) -> list:
        images = get_user_own_review_links(pk=_id)
        if self.get_error(images):
            self.errors.append(
                'Problem with getting user`s reviews images.')
            return
        return images

    def _get_all_users_review_id(self, _id: int) -> list:
        ids = get_user_own_review_ids(pk=_id)
        if self.get_error(ids):
            self.errors.append(
                'Problem with getting user`s reviews images.')
            return
        return ids

    def _get_all_users_review_album_title(self, _id: int) -> list:
        titles = get_user_own_review_album_title(pk=_id)
        if self.get_error(titles):
            self.errors.append(
                'Problem with getting user`s reviews titles.')
            return
        return titles
