
#from utils.abstractions.interfaces.i_command import ICommand
from utils.abstractions.data_structures.service_errors import ServiceErrors
from utils.abstractions.interfaces.i_use_case import IUseCase

class BaseService(IUseCase):
    def __init__(self) -> None:
        self._errors: ServiceErrors = ServiceErrors()
        self._got_entities = []

    def execute(self):
        raise NotImplementedError()

    @property
    def is_error(self) -> bool:
        if len(self.errors) != 0:
            return True
        return False
    
    @property
    def response(self) -> list:
        if self.is_error:
            return {[]}
        return self._got_entities 

    @property
    def errors(self) -> ServiceErrors:
        return self._errors

