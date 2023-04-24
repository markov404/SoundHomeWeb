from utils.abstractions.abstract_classes.abs_file_manager import ABSFileManager

class LogProvider:
    def read_logs(self, path: str) -> str:
        abstract_file_manager = ABSFileManager(path)
        data = abstract_file_manager.read()
        return data
