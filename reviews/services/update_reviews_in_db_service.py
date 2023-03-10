import threading

from reviews.services.interfaces.ICommand import ICommand
from reviews.components.pitchf_scruber_builder import PitchFScrubberBuilder
from reviews.components.translator import Translator
from reviews.components.speecher import SpeecherBasedYaCloudTech

from reviews.components.database_requests import (
    delete_all_active_review_objects,
    create_new_review_and_extends_records)


class UpdateReviewsInDBService(ICommand):

    def execute(self):
        new_data = self._scrub_new_data()
        new_data = self._change_data_structure(new_data)

        self._translate_reviews(new_data)
        self._make_audio_revs(new_data)

        self._update_database(new_data)

    def _scrub_new_data(self) -> list[dict]:
        scruber = PitchFScrubberBuilder().build()
        scruber.update_data()  
        data = scruber.get_actual_data()
        scruber.quit_driver()

        del scruber

        return data

    def _translate_reviews(self, data: list[dict]) -> None:
        trns = Translator()
        for point in data:
            text = point['record_data']['review_text']
            translated = trns.translate(text)
            point['translation'] = translated

        del trns
    
    def _make_audio_revs(self, data: list[dict]) -> None:
        spchr = SpeecherBasedYaCloudTech()
        threads = []
        results = [{} for x in data]
        for i, point in enumerate(data):
            text = point['translation']
            nt = threading.Thread(
                target=spchr.get_speech_file_object, 
                args=(text, i, results)
                )
            nt.start()
            threads.append(nt)

        for process in threads:
            process.join()

        del spchr
        
        for rslt, point in zip(results, data):
            point['audio_bytes'] = rslt

    def _update_database(self, data: list[dict]) -> None:
        
        delete_all_active_review_objects()

        for point in data:
            try:
                create_new_review_and_extends_records(point)
            except:
                pass

    def _change_data_structure(self, data: list[dict]) -> list[dict]:
        new_data_structure = []

        for record in data:
            new_data_structure.append(
                {
                    'record_data': record, 
                    'translation': None,
                    'audio_bytes': None
                    })

        return new_data_structure