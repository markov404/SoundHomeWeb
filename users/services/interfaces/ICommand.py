
from abc import ABC, abstractmethod


class ICommand(ABC):
    @abstractmethod
    def execute():
        raise NotImplementedError()
