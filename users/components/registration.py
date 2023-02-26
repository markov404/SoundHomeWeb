
from ..models import SoundHomeUsers
from schema import Schema
import re

from .interfaces.i_registration import IRegistrationBase

class Registration(IRegistrationBase):
    email_pattern = re.compile(r"[^@]+@[^@]+\.[^@]+")

    def create_user(self, email, password):
        # user = User.objects.create_user(email=email, password=password)
        # user.save()
        # return bool(self.email_pattern.match(email))
        pass

