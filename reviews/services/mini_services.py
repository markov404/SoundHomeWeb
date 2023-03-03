
from reviews.services.interfaces.ICommand import ICommand
from reviews.components.database_requests import get_latest_review_id

class LatestReviewId(ICommand):
    
    def execute(self):
        return self._extract_latest_review_id()

    def _extract_latest_review_id(self):
        return get_latest_review_id()
        