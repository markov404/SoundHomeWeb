
import json
from utils.abstractions.interfaces.i_use_case import IUseCase
from utils.abstractions.types.error_type import Error

from logging import getLogger

log = getLogger(__name__)


class ServiceErrors(list):
    def __init__(self, used_by) -> None:
        if not isinstance(used_by, IUseCase):
            raise TypeError('Service error should have IUseCase based used_by!')
        self.USED_BY = used_by

    def append(self, message: str, code: int = None):
        if code is None:
            er = Error(message=message)
            super().append(er)
        else:
            er = Error(message=message, code=code)
            super().append(er)
        log.warning(f'service({self.USED_BY}) got error({er})')

    @property
    def type_of_server(self) -> bool:
        for error in self:
            if self.__error_code_type_of_server(error['code']):
                return True
        return False
    
    def __error_code_type_of_server(self, code) -> bool:
        if (code // 100) == 5:
            return True
        return False

    def as_json(self) -> str:
        return json.dumps(self)
    
    def as_messages(self) -> list:
        output = []
        for error in self:
            output.append(error['message'])
        return output
