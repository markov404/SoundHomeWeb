from PIL import Image

from django.core.files.uploadedfile import InMemoryUploadedFile
from utils.abstractions.interfaces.i_validator import IValidator

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

class TextValidator(IValidator):
    def __init__(self, max_lenght=500) -> None:
        super().__init__()
        self.max_lenght = max_lenght

    def is_valid(self, text: str) -> bool:
        return self._validate(text)
    
    def _validate(self, text: str) -> bool:
        if not isinstance(text, str):
            return False
        return True