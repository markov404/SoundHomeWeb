
from abc import ABC, abstractmethod

class IUseCase(ABC):
    @abstractmethod
    def execute():
        raise NotImplementedError()
    
    @property
    @abstractmethod
    def is_error():
        raise NotImplementedError()

    @property
    @abstractmethod
    def errors():
        raise NotImplementedError()

    @property
    @abstractmethod
    def response():
        raise NotImplementedError()
