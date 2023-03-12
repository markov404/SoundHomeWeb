
from django import forms
from reviews.models import UserReview
from utils.abstractions.abstract_classes.abs_forms import BaseLayerValidationForm

class UserReviewForm(BaseLayerValidationForm):
    class Meta:
        model = UserReview
        fields = ['score', 'image', 'album_title', 'album_author', 'review_title', 'review_text']


class UsersReviewAllForm(forms.Form):
    page = forms.IntegerField()
    