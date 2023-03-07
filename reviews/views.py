

from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.http import require_http_methods

from utils.wrappers import logged_in_user_only
from utils.sesssion import user_id

from reviews.services.all_reviews_page_service import AllReviewsPageSerive
from reviews.services.certain_review_page_service import CertainReviewPageService
from reviews.services.create_user_review_service import CreateUserReviewService
from reviews.services.all_users_reviews_page_service import AllUsersReviewsPageService
from reviews.services.certain_user_review_page_service import CertainUserReviewPageService

# Create your views here.

@require_http_methods(["GET"])
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
            'translation': translation, 'audio_url': audio_url,
            'PRO': True})


@require_http_methods(["GET"])
@logged_in_user_only()
def all_reviews(request: WSGIRequest):
    data = AllReviewsPageSerive().execute()
    if data is None:
        status = 'error'
    else:
        status = 'success'
        
    return render(request, 'reviews/all_reviews.html', context={'data': data, 'status': status, 'title': 'PRO Reviews', 'PRO': True})


@require_http_methods(["POST"])
@logged_in_user_only()
def post_user_review(request: WSGIRequest):
    usr_id = user_id(request)
    data = CreateUserReviewService().execute(_id=usr_id, request=request)
    
    if data['status'] == 'success':
        return redirect(reverse('ceraint_user_review', kwargs={ 'pk': data['review_id'] }))
    else:
        return render('fdf')


@require_http_methods(["GET"])
@logged_in_user_only()
def all_users_reviews(request: WSGIRequest):
    data = AllUsersReviewsPageService().execute()
    if data is None:
        status = 'error'
    else:
        status = 'success'
        
    return render(request, 'reviews/all_reviews.html', context={'data': data, 'status': status, 'title': 'Amateur Reviews'})


@require_http_methods(["GET"])
@logged_in_user_only()
def index_user_reviews(request: WSGIRequest, pk: int):
    response = CertainUserReviewPageService().execute(pk)
    
    data = response['data']
    next_id = response['next_id']
    prev_id = response['prev_id']
    nickname = response['author_nickname']

    return render(
        request, 'reviews/review.html', 
        context={'data': data, 
            'additional_info': {'next_id': next_id, 'prev_id': prev_id, 'nickname': nickname}})