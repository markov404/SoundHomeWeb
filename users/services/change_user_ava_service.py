
from django.core.files.uploadedfile import InMemoryUploadedFile

from utils.abstractions.abstract_classes.abs_services import BaseService
from users.components.database_requests import update_user_additional_image

class ChangeUserAvaService(BaseService):
    MANDATORY_FIELDS = {'image'}
    def execute(self, data: dict, _id: int):
        super().execute(data=data)
        
        image = data['image']

        if not self._update_usr_image(_id=_id, image=image):
            self.errors.append('Data base exception')

    def _update_usr_image(self, _id: int, image: InMemoryUploadedFile) -> InMemoryUploadedFile:
        return update_user_additional_image(pk=_id, ava=image)
