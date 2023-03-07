
from reviews.models import Review
from reviews.components.database_requests import get_all_reviews_data_list
from reviews.services.interfaces.ICommand import ICommand

class AllReviewsPageSerive(ICommand):
    
    def execute(self):
        data = self._extract_all_reviews_data_list()
        return data

    def _extract_all_reviews_data_list(self) -> list[dict] | None:
        return get_all_reviews_data_list()
