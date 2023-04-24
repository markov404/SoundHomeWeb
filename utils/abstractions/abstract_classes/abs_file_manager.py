from utils.abstractions.interfaces.i_file_manager import IFileManager
from utils.abstractions.types.error_type import Error
from logging import getLogger

log = getLogger(__name__)


class ABSFileManager(IFileManager):
    def __init__(self, path: str) -> None:
        self.path = path

    def read(self) -> str | Error:
        output: str = ''
        try:
            with open(self.path, 'r') as file:
                output = file.read()
            return output
        except Exception as E:
            log.warning(f'{E}')
            return Error(
                f'No such file in directory {self.path}', 500)
    
    def write(self, data: str) -> None:
        """ Writing string argument to file """
        with open(self.path, 'w', encoding='utf-8') as file:
            file.write(data)
