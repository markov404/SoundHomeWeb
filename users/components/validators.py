
import re
from PIL import Image

from django.core.files.uploadedfile import InMemoryUploadedFile
from users.components.interfaces.i_validator import IValidator


class ImageValidator(IValidator):

    def is_valid(self, image: InMemoryUploadedFile) -> bool:
        return self._validate(image)[0]
    
    def _validate(self, image: InMemoryUploadedFile) -> list:
        try:
            im = Image.open(image)
            output = True
        except:
            im = None
            output = False

        return [output, im]
    
    def exctract_image(self, image: InMemoryUploadedFile):
        try:
            im = Image.open(image)
        except:
            im = None
        
        return im


class UserAvaValidator(ImageValidator):
    def is_valid(self, image: InMemoryUploadedFile) -> bool:
        st1 = super().is_valid(image)
        if not st1:
            return False
        
        image_file = self.exctract_image(image)
        return self._size_validation(image_file)
        
    def _size_validation(self, image_file: Image):
        width, height = image_file.size
        if width > 1000 and height > 1000:
            return False
        return True


class TextValidator(IValidator):
    def is_valid(self, text: str) -> bool:
        return self._validate(text)
    
    def _validate(self, text: str) -> bool:
        if not isinstance(text, str):
            return False
        return True


class UserNicknameValidator(TextValidator):
    nickname_pattern = re.compile(r"[^0-9][^@#]+")

    def is_valid(self, text: str) -> bool:
        st1 = super().is_valid(text)
        st2 = len(text) <= 50
        st3 = bool(re.fullmatch(self.nickname_pattern, text))

        return (st1 and st2 and st3)
