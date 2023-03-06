
from users.services.interfaces.ICommand import ICommand
from users.components.database_requests import (
    get_user_email_by_pk,
    get_user_additional_image_url,
    get_user_additional_nickname)


class UserBasicDataService(ICommand):
    
    def execute(self, id: int):
        if id is None:
            return {'status': 'error'}

        email = self._extract_basic_user_data(id)
        nickname = self._extract_user_nickname(id)
        image = self._extract_user_ava_url(id)

        return {
            'status': 'success', 
            'data': {
                'email': email,
                'nickname': nickname,
                'image': image
                }
                }

    def _extract_basic_user_data(self, id: int) -> str | None:
        return get_user_email_by_pk(id)

    def _extract_user_ava_url(self, id: int) -> str | None:
        return get_user_additional_image_url(id)

    def _extract_user_nickname(self, id: int) -> str | None:
        return get_user_additional_nickname(id)