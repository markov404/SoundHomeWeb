
from users.services.interfaces.ICommand import ICommand
from users.components.validators import UserNicknameValidator
from users.components.database_requests import update_user_additional_nickname

class ChangeUserNicknameService(ICommand):
    
    def execute(self, request, _id):
        nickname = self._extract_new_ava(request)
        if nickname is None:
            return {"status": "error"}

        if not UserNicknameValidator().is_valid(nickname):
            return {"status": "error"}

        update_user_additional_nickname(pk=_id, text=nickname)
        return {"status": "success"}

    def _extract_new_ava(self, request) -> str | None:
        try:
            nickname = request.POST.get("user_nickname")
        except:
            nickname = None
        
        return nickname
