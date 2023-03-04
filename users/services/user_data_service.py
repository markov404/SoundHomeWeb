
from users.services.interfaces.ICommand import ICommand
from users.components.database_requests import (
    get_user_email_by_pk,
    get_user_additional_info_by_pk)


class UserBasicDataService(ICommand):
    
    def execute(self, id: int):
        if id is None:
            return {'status': 'error'}

        email = self._extract_basic_user_data(id)
        response = self._extract_additional_user_data(id)

        response.update({'email': email})

        return {'status': 'success', 'data': response}

    def _extract_basic_user_data(self, id: int) -> str | None:
        return get_user_email_by_pk(id)
    
    def _extract_additional_user_data(self, id: int) -> dict | None:
        return get_user_additional_info_by_pk(id)
