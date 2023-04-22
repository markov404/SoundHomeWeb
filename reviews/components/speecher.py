
from gtts import gTTS
from io import BytesIO
import textwrap

from reviews.components.interfaces.ISpeecher import ISpeecher
from reviews.components.ya_api_speech_kit_client_v1 import YandexAPISpeechKitV1Client


class Speecher(ISpeecher):

    def get_speech_file_object(self, text: str) -> BytesIO:
        gtts_object = gTTS(text=text, lang='ru', slow=False)
        container = BytesIO()
        gtts_object.write_to_fp(container)

        del gtts_object
        return container


class SpeecherModifiedForAsync(ISpeecher):

    def get_speech_file_object(
            self,
            text: str,
            tid: int,
            _return: list) -> None:
        gtts_object = gTTS(text=text, lang='ru', slow=False)
        container = BytesIO()
        gtts_object.write_to_fp(container)

        del gtts_object
        _return[tid] = container


class SpeecherBasedYaCloudTech(ISpeecher):

    def get_speech_file_object(
            self,
            text: str,
            tid: int,
            _return: list) -> None:
        text_chunks = self._chunks(text)

        bytes_: bytes = b''
        for chunk in text_chunks:
            bytes_response = YandexAPISpeechKitV1Client().synthesize(text=chunk)
            bytes_ += (bytes_response)

        container = BytesIO(bytes_)

        del bytes_response
        _return[tid] = container

    def _chunks(self, text: str, s: int = 4999) -> list[str]:
        return textwrap.wrap(text=text, width=s)
