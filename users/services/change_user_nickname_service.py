
from users.components.database_requests import update_user_additional_nickname
from utils.abstractions.abstract_classes.abs_services import BaseService


class ChangeUserNicknameService(BaseService):
    MANDATORY_FIELDS = {'nickname'}

    def execute(self, data: dict, _id: int):
        super().execute(data=data)

        nickname = data['nickname']

        if self.get_error(
            update_user_additional_nickname(
                pk=_id,
                text=nickname)):
            self.errors.append('Database error')

    def _update_nickname(self, _id: int, nickname: str):
        return update_user_additional_nickname(pk=_id, text=nickname)
