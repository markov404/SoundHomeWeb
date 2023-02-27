
from schema import Schema
import re
import hashlib

from ..models import SoundHomeUsers

from .interfaces.i_registration import IRegistrationBase

class Registration(IRegistrationBase):
    email_pattern = re.compile(r"[^@]+@[^@]+\.[^@]+")

    def create_user(self, email, password):
        try:
            user = SoundHomeUsers(email=email, password=self.__passw_hex(password))
            user.save()
        except:
            return False
        else:
            return user

    def __passw_hex(self, password: str):
        return hashlib.sha256(password.encode()).hexdigest()

