
from abc import ABC, abstractmethod

class IValidator(ABC):

    @abstractmethod
    def is_valid():
        raise NotImplementedError()
        