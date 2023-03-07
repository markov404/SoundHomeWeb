
from django.core.files.uploadedfile import InMemoryUploadedFile
from users.services.interfaces.ICommand import ICommand
from users.components.validators import UserAvaValidator
from users.components.database_requests import update_user_additional_image

class ChangeUserAvaService(ICommand):
    
    def execute(self, request, _id):
        image = self._extract_new_ava(request)
        if image is None:
            return {"status": "error"}

        if not UserAvaValidator().is_valid(image):
            return {"status": "error"}

        update_user_additional_image(pk=_id, ava=image)
        return {"status": "success"}

    def _extract_new_ava(self, request) -> InMemoryUploadedFile:
        try:
            image = request.FILES.get("user_image")
        except:
            image = None
        
        return image
