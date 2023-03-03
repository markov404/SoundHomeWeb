
from gtts import gTTS
from io import BytesIO

from reviews.components.interfaces.ISpeecher import ISpeecher

class Speecher(ISpeecher):

    def get_speech_file_object(self, text: str) -> BytesIO:
        gtts_object = gTTS(text=text, lang='ru', slow=False)
        container = BytesIO()
        gtts_object.write_to_fp(container)
        
        del gtts_object
        return container


class SpeecherModifiedForAsync(ISpeecher):

    def get_speech_file_object(self, text: str, tid: int, _return: list) -> None:
        gtts_object = gTTS(text=text, lang='ru', slow=False)
        container = BytesIO()
        gtts_object.write_to_fp(container)
        
        del gtts_object
        _return[tid] = container
