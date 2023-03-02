
from abc import ABC, abstractmethod

class IDriverAdapter(ABC):

    @abstractmethod
    def get_element():
        """Getting selenium element object"""
        raise NotImplementedError()
    
    @abstractmethod
    def get_all_elements():
        """Getting list of selenium element objects"""
        raise NotImplementedError()

    @abstractmethod
    def click_on_element():
        """Clicks on element"""
        raise NotImplementedError()
    
    @abstractmethod
    def go_to_page():
        """Change page"""
        raise NotImplementedError()
    
    @abstractmethod
    def reload_page():
        """Reloads page"""
        raise NotImplementedError()
        