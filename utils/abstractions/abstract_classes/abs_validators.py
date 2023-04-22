from PIL import Image

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.files.uploadedfile import InMemoryUploadedFile
from utils.abstractions.interfaces.i_validator import IValidator


class AbstractValidator(IValidator):
    def is_valid(self):
        pass

    def error(self, msg: str, value: any) -> ValidationError:
        raise ValidationError(
            _(msg),
            params={'value': value}
        )


class ImageValidator(AbstractValidator):

    def is_valid(
            self,
            image: InMemoryUploadedFile) -> InMemoryUploadedFile | ValidationError:
        try:
            im = Image.open(image)
        except BaseException:
            self.error(
                f'This image is not even an image', image)
        else:
            return image

    def exctract_image(self, image: InMemoryUploadedFile) -> Image:
        try:
            im = Image.open(image)
        except BaseException:
            im = None

        return im


class TextValidator(AbstractValidator):
    def __init__(self, max_lenght=500) -> None:
        super().__init__()
        self.max_lenght = max_lenght

    def is_valid(self, text: str) -> str | ValidationError:
        return self._validate(text)

    def _validate(self, text: str) -> str | ValidationError:
        if not isinstance(text, str):
            self.error(f'This text is not even a text', text)
        return text
