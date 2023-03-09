
from users.components.database_requests import add_user_ava_and_nickname_end_set_user_active
from utils.abstractions.abstract_classes.abs_services import BaseService


class SetUpProfileService(BaseService):
    MANDATORY_FIELDS = {'image', 'nickname'}

    def execute(self, data: dict, _id: int):        
        super().execute(data=data)

        image = data['image']
        nickname = data['nickname']

        if self.get_error(self._set_up_account(_id, image, nickname)):
            self.errors.append('Database error')
    
    def _set_up_account(self, _id: int, image, nickname) -> dict:
        return add_user_ava_and_nickname_end_set_user_active(
            pk=_id, ava=image, nickname=nickname)
            