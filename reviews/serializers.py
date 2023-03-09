
from reviews.models import UserReview
from utils.abstractions.abstract_classes.abs_form import BaseLayerValidationForm

class UserReviewForm(BaseLayerValidationForm):
    class Meta:
        model = UserReview
        fields = ['score', 'image', 'album_title', 'album_author', 'review_title', 'review_text']
