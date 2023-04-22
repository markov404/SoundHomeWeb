
# from utils.abstractions.interfaces.i_command import ICommand
from utils.abstractions.data_structures.service_errors import ServiceErrors
from utils.abstractions.data_structures.service_response import ServiceResponse
from utils.abstractions.types.error_type import Error
from utils.abstractions.interfaces.i_use_case import IUseCase


class BaseService(IUseCase):
    MANDATORY_FIELDS = set()

    def __init__(self) -> None:
        self._errors: ServiceErrors = ServiceErrors(self)
        self._got_entities: ServiceResponse = ServiceResponse()

    def execute(self, data):
        if not (set(data.keys()) == self.MANDATORY_FIELDS):
            self.errors.append('Form field names dont correct', 400)
            return

    @property
    def is_error(self) -> bool:
        if len(self.errors) != 0:
            return True
        return False

    @property
    def response(self) -> ServiceResponse:
        if self.is_error:
            return ServiceResponse()
        return self._got_entities

    @property
    def errors(self) -> ServiceErrors:
        return self._errors

    def get_error(self, value) -> bool:
        if isinstance(value, Error):
            return True
        return False
