
from abc import ABC, abstractmethod

class ISpeechKitApi(ABC):

    @abstractmethod
    def synthesize():
        raise NotImplementedError()
        