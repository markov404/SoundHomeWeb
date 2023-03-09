
from utils.abstractions.abstract_classes.abs_services import BaseService
from users.components.database_requests import (
    get_user_email_by_pk,
    get_user_additional_image_url,
    get_user_additional_nickname)


class UserBasicDataService(BaseService):
    
    def execute(self, _id: int):
        if _id is None:
            raise Exception(f'{self.execute} should get _id of user.')

        email = self._extract_basic_user_data(_id)
        nickname = self._extract_user_nickname(_id)
        image = self._extract_user_ava_url(_id)

        if not self.is_error:
            response_object = {'email': email, 'nickname': nickname, 'image': image}
            self._got_entities.append(response_object)

    def _extract_basic_user_data(self, _id: int) -> str | None:
        email = get_user_email_by_pk(_id)
        if not email:
            self.errors.append('Proble with getting email')
        return email

    def _extract_user_ava_url(self, _id: int) -> str | None:
        image_url = get_user_additional_image_url(_id)
        if not image_url:
            self.errors.append('Problem with getting image url')
        return image_url

    def _extract_user_nickname(self, _id: int) -> str | None:
        nickname = get_user_additional_nickname(_id)
        if not nickname:
            self.errors.append('Problem with getting nickname')
        return nickname