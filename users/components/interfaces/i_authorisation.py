

from abc import ABC, abstractmethod


class IAuthorisationBase(ABC):

    @abstractmethod
    def login(self):
        raise NotImplementedError()

    @abstractmethod
    def logout(self):
        raise NotImplementedError()
