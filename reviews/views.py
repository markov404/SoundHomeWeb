

from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from utils.wrappers import logged_in_user_only

from reviews.services.all_reviews_page_service import AllReviewsPageSerive
from reviews.services.certain_review_page_service import CertainReviewPageService

# Create your views here.

@logged_in_user_only()
def index_reviews(request: WSGIRequest, pk: int):
    response = CertainReviewPageService().execute(pk)
    
    data = response['data']
    translation = response['translation']
    next_id = response['next_id']
    prev_id = response['prev_id']
    audio_url = response['audio_url']

    return render(
        request, 'reviews/review.html', 
        context={
            'data': data, 
            'additional_info': {'next_id': next_id, 'prev_id': prev_id}, 
            'translation': translation, 'audio_url': audio_url})

@logged_in_user_only()
def all_reviews(request: WSGIRequest):
    data = AllReviewsPageSerive().execute()
    if data is None:
        status = 'error'
    else:
        status = 'success'
        
    return render(request, 'reviews/all_reviews.html', context={'data': data, 'status': status})
