
from .interfaces.IReviewsPage import IReviewsPageBase
from ..models import Review


class ReviewsPage(IReviewsPageBase):
    
    def get_all_reviews_data(self):
        revs = Review.objects.all()
        if len(revs) == 0:
            return None
        else:
            output = []
            for item in revs:
                output.append(item.__dict__)
            return output

    def get_review_by_id(self):
        pass
    
    def __extract_objects_data(self, objs: list):
        pass
