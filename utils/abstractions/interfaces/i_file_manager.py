from abc import ABC, abstractmethod


class IFileManager(ABC):
    @abstractmethod
    def read(self):
        raise NotImplementedError()
    
    @abstractmethod
    def write(self):
        raise NotImplementedError()
