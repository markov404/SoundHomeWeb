
from users.services.interfaces.ICommand import ICommand
from users.components.validators import UserAvaValidator, UserNicknameValidator
from users.components.database_requests import add_user_ava_and_nickname, change_user_active

class SetUpProfileService(ICommand):
    
    def execute(self, request, _id: int):
        rsp = self._extract_data_from_request(request)
        if rsp is None:
            return {"status": "error", "message": "UnvalidRequest"}
        
        image = rsp['image']
        nickname = rsp['nickname']

        if not UserNicknameValidator().is_valid(nickname):
            return {"status": "error", "message": "Unvalid symbols for nickname!"}

        if not UserAvaValidator().is_valid(image):
            return {"status": "error", "message": "Unvalid image"}

        self._add_user_data(_id, image, nickname)
        if self._set_user_active(_id) is not None:
            return {"status": "success"}


    def _extract_data_from_request(self, request):
        try:
            image = request.FILES.get("image")
            nickname = request.POST.get("nickname")

            output = {'image': image, 'nickname': nickname}
        except:
            output = None

        return output

    def _add_user_data(self, _id, image, nickname):
        return add_user_ava_and_nickname(_id, image, nickname)

    def _set_user_active(self, _id):
        return change_user_active(_id, True)