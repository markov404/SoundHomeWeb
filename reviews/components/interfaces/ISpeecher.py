
from abc import ABC, abstractmethod


class ISpeecher(ABC):

    @abstractmethod
    def get_speech_file_object():
        raise NotImplementedError()
