
from reviews.components.database_requests import get_all_reviews_data_list
from utils.abstractions.abstract_classes.abs_services import BaseService

class AllReviewsPageSerive(BaseService):
    
    def execute(self):
        self._extract_all_reviews_data_list()

    def _extract_all_reviews_data_list(self) -> None:
        data = get_all_reviews_data_list()
        if self.get_error(data):
            self.errors.append('Problem with getting reviews data')
            return
        self._got_entities.append({'data': data})
