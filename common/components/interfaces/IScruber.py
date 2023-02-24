

from abc import ABC, abstractmethod


class IScruber(ABC):
    @abstractmethod
    def update_data():
        """Updating new info to database."""
        pass

    @abstractmethod
    def get_actual_data():
        """Getting actual data from database."""
        pass

