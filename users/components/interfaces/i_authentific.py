

from abc import ABC, abstractmethod

class IAuthentificationBase(ABC):

    @abstractmethod
    def is_user_exists(self):
        raise NotImplementedError()
    
    @abstractmethod
    def is_password_right(self):
        raise NotImplementedError()
    