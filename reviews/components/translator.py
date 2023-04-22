
import textwrap

from deep_translator import GoogleTranslator
from reviews.components.interfaces.ITranslator import ITranslator


class Translator(ITranslator):
    def __init__(
            self,
            source: str = 'english',
            lang: str = 'ru') -> None:

        self.__translator = GoogleTranslator(
            source='english', target=lang)

    def translate(self, text: str) -> str:
        chs: list[str] = self._chunks(text)
        translated_text = ""

        for chunk in chs:
            translated_text += f' {self.__translator.translate(chunk)}'
        return translated_text

    def _chunks(self, text: str, s: int = 4999) -> list[str]:
        return textwrap.wrap(text=text, width=s)
