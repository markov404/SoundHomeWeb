
from utils.abstractions.abstract_classes.abs_services import BaseService
from users.components.database_requests import (
    get_user_email_by_pk,
    get_user_additional_image_url,
    get_user_additional_nickname,
    get_user_own_review_links,
    get_user_own_review_ids,
    get_user_favourites_reviews)


class UserBasicDataService(BaseService):

    def execute(self, _id: int):
        if _id is None:
            raise Exception(f'{self.execute} should get _id of user.')

        self._extract_basic_user_data(_id)
        self._extract_user_nickname(_id)
        self._extract_user_ava_url(_id)
        self._extract_user_reviews(_id)
        self._extract_user_fav_reviews(_id)

    def _extract_basic_user_data(self, _id: int) -> None:
        email = get_user_email_by_pk(_id)
        if self.get_error(email):
            self.errors.append('Proble with getting email')
            return
        self._got_entities.append({'email': email})

    def _extract_user_ava_url(self, _id: int) -> None:
        image_url = get_user_additional_image_url(_id)
        if self.get_error(image_url):
            self.errors.append('Problem with getting image url')
            return
        self._got_entities.append({'image': image_url})

    def _extract_user_nickname(self, _id: int) -> None:
        nickname = get_user_additional_nickname(_id)
        if self.get_error(nickname):
            self.errors.append('Problem with getting nickname')
            return
        self._got_entities.append({'nickname': nickname})

    def _extract_user_reviews(self, _id: int) -> None:
        links = self._extract_users_own_review_image_urls(_id)
        ids = self._extract_users_own_review_image_ids(_id)

        output = []
        for link, _id in zip(links, ids):
            output.append({'image': link, 'id': _id})

        if len(output) == 0:
            return None
        elif len(output) > 4:
            self._got_entities.append(
                {'reviews': True, 'reviews_type_make': True})
        else:
            self._got_entities.append(
                {'reviews': output, 'reviews_amount': len(output)})

    def _extract_users_own_review_image_ids(self, _id: int) -> list | bool:
        ids = get_user_own_review_ids(pk=_id)
        if self.get_error(ids):
            self.errors.append('Problem with getting user reveiws')
        return ids

    def _extract_users_own_review_image_urls(self, _id: int) -> list | bool:
        links = get_user_own_review_links(pk=_id)
        if self.get_error(links):
            self.errors.append('Problem with getting user reveiws')
        return links

    def _extract_user_fav_reviews(self, _id: int) -> None:
        rvws = get_user_favourites_reviews(_id)
        if self.get_error(rvws):
            self.errors.append('Problem with getting fav reviews images')
            return

        if len(rvws) == 0:
            return None
        elif len(rvws) > 6:
            self._got_entities.append(
                {'fav_reviews': True, 'fav_reviews_alot': True})
        else:
            self._got_entities.append({'fav_reviews': rvws})
