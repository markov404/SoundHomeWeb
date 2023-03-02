
from abc import ABC, abstractmethod

class IBuilder(ABC):

    @abstractmethod
    def build():
        raise NotImplementedError()
        