
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

    def get_review_by_id(self, id: int):
        rev = Review.objects.get(pk=id)
        if rev is not None:
            return rev.__dict__
        else:
            return None
    
    def get_latest_id(self):
        return Review.objects.latest('id').id

    def __extract_objects_data(self, objs: list):
        pass
