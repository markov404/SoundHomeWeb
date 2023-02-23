
import hashlib
from ..models import SoundHomeUsers

class Authentification:
    def is_user_exists(self, email):
        u = SoundHomeUsers.objects.get(email=email)

        if u is not None:
            return u.pk
        else:
            return None
    
    def is_password_right(self, pk, password):
        u = SoundHomeUsers.objects.get(pk=pk)

        return u.password == self.__passw_hex(password)
    
    def __passw_hex(self, password: str):
        return hashlib.sha256(password.encode()).hexdigest()
