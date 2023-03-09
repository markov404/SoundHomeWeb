
from users.components.database_requests import update_user_additional_nickname
from utils.abstractions.abstract_classes.abs_services import BaseService

class ChangeUserNicknameService(BaseService):
    
    def execute(self, data: dict, _id: int):
        nickname = data['nickname']

        if not update_user_additional_nickname(pk=_id, text=nickname):
            self.errors.append('Database error')

    def _update_nickname(self, _id: int, nickname: str):
        return update_user_additional_nickname(pk=_id, text=nickname)
