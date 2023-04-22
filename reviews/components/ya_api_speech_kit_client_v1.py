
import os
import requests

from reviews.components.interfaces.ISpeecherClient import ISpeechKitApi


class YandexAPISpeechKitV1Client(ISpeechKitApi):
    API_MAP = {
        'synthesize': 'https://tts.api.cloud.yandex.net/speech/v1/tts:synthesize'}

    def __init__(self) -> None:
        iam_token = os.getenv('YANDEX_CLOUD_IAM_TOKEN')
        folder_id = os.getenv('YANDEX_CLOUD_FOLDER_ID')

        if (iam_token is None) or (folder_id is None):
            raise Exception('Environmental variables is not setupped.')
        self.__iam_token = iam_token
        self.__folder_id = folder_id

    def synthesize(self, text: str, lang: str = 'ru-RU') -> bytes:
        headers = {
            'Authorization': 'Bearer ' + self.__iam_token,
        }
        data = {
            'text': text,
            'lang': lang,
            'voice': 'filipp',
            'folderId': self.__folder_id,
            'format': 'mp3',
            'sampleRateHertz': 48000,
        }
        url = self.API_MAP['synthesize']

        response = requests.post(url=url, headers=headers, data=data)
        if response.status_code != 200:
            raise RuntimeError(
                "Invalid response received: code: %d, message: %s" %
                (response.status_code, response.text))

        return response.content
