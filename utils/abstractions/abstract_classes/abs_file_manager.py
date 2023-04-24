from utils.abstractions.interfaces.i_file_manager import IFileManager


class ABSFileManager(IFileManager):
    def __init__(self, path: str) -> None:
        self.path = path

    def read(self) -> str:
        output: str = ''
        with open(self.path, 'r') as file:
            output = file.read()
        return output
    
    def write(self, data: str) -> None:
        """ Writing string argument to file """
        with open(self.path, 'w', encoding='utf-8') as file:
            file.write(data)
