
from utils.abstractions.abstract_classes.abs_services import BaseService
from users.components.database_requests import get_user_additional_active_status


class UserActiveDataService(BaseService):
    def execute(self, _id):
        status = self._extract_active_boolean(_id)

        if not self.is_error:
            self._got_entities.append({'active': status})

    def _extract_active_boolean(self, _id):
        status = get_user_additional_active_status(_id)
        if self.get_error(status):
            self.errors.append('Query error')
            return

        return status
