

from abc import ABC, abstractmethod


class IRegistrationBase(ABC):

    @abstractmethod
    def create_user(self):
        raise NotImplementedError()
