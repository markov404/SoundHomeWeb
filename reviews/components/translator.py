
from deep_translator import GoogleTranslator
from reviews.components.interfaces.ITranslator import ITranslator

class Translator(ITranslator):
    def __init__(
        self, 
        source: str = 'english', 
        lang: str ='ru') -> None:

        self.__translator = GoogleTranslator(
            source='english', target=lang)

    def translate(self, text: str) -> str:
        return str(self.__translator.translate(text))
