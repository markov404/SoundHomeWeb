
import json
from utils.abstractions.types.error_type import Error

class ServiceErrors(list):
    def append(self, message: str, code: int = None):
        if code is None:
            super().append(Error(message=message))
        else:
            super().append(Error(message=message, code=code))

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

    def as_json(self):
        return json.dumps(self)       
