
from reviews.services.interfaces.ICommand import ICommand
from reviews.models import Review

class LatestReviewId(ICommand):
    
    def execute(self):
        return self._extract_latest_review_id()

    def _extract_latest_review_id(self):
        try:
            qs = Review.objects.all().filter(active=True)
            latest = qs.reverse()[0].pk
        except:
            latest = None

        return latest    