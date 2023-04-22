
from abc import ABC, abstractmethod


class IReviewsPageBase(ABC):

    @abstractmethod
    def get_all_reviews_data():
        pass

    @abstractmethod
    def get_review_by_id():
        pass
