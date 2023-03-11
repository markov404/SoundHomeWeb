
import re
from PIL import Image

from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from django.core.files.uploadedfile import InMemoryUploadedFile
from utils.abstractions.abstract_classes.abs_validators import ImageValidator, TextValidator


class UserAvaValidator(ImageValidator):
    def is_valid(self, value: InMemoryUploadedFile) -> InMemoryUploadedFile | ValidationError:
        super().is_valid(value)
        image_file = self.exctract_image(value)
        return self._size_validation(image_file, value)
        
    def _size_validation(self, image_file: Image, value: InMemoryUploadedFile):
        width, height = image_file.size
        if (width > 1000) or (height > 1000) or ((width > 1000) and (height > 1000)):
            self.error(f'Your image is out of maximum size.', value)
        return value


class UserNicknameValidator(TextValidator):
    nickname_pattern = re.compile(r"[^0-9][^@#]+")

    def is_valid(self, value: str) -> str | ValidationError:
        super().is_valid(value)
        if not (len(value) <= 50):
            self.error(f'{value} is out of size', value)
        
        if not (bool(re.fullmatch(self.nickname_pattern, value))):
            self.error(f'Dont use @ in middle of nickname.', value)

        return value


class UserEmailValidator(TextValidator):
    default_email_validator = EmailValidator(message='Type in correct email, please', code=69, allowlist=['yandex.ru'])
    black_list = ['mail.ru']

    def is_valid(self, value: str) -> str | ValidationError:
        super().is_valid(value)
        self.default_email_validator(value)
        if value.split('@')[1] in self.black_list:
            self.error(f'We are not supporting mail.ru domain.', value)
        return value

            
class UserPasswordValidator(TextValidator):
    password_pattern = re.compile(r"(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}")

    def is_valid(self, value: str) -> str | ValidationError:
        super().is_valid(value)
        if not (len(value) < 50):
            self.error(f'Password should be maximum 50 characters', value)
        
        if not bool(re.fullmatch(self.password_pattern, value)):
            self.error(
                f'Password should have minimum eight chars, at least one letter, and one numeber', 
                value)

        return value
