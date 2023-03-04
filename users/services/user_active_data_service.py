

from users.services.interfaces.ICommand import ICommand
from users.components.database_requests import get_user_additional_active_status

class UserActiveDataService(ICommand):
    def execute(self, id):
        return self._extract_active_boolean(id)

    def _extract_active_boolean(self, id):
        return get_user_additional_active_status(id)