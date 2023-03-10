

from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import redirect, render
from django.http import JsonResponse, HttpResponseServerError
from django.urls import reverse
from django.views.decorators.http import require_http_methods

from utils.wrappers import logged_in_user_only
from utils.sesssion import user_id

from reviews.services.all_reviews_page_service import AllReviewsPageSerive
from reviews.services.certain_review_page_service import CertainReviewPageService
from reviews.services.create_user_review_service import CreateUserReviewService
from reviews.services.all_users_reviews_page_service import AllUsersReviewsPageService
from reviews.services.certain_user_review_page_service import CertainUserReviewPageService
from reviews.services.mini_services import DoUserLikeReviewWithId
from reviews.services.mini_services import LikeOrUnlikeIt

from reviews.serializers import UserReviewForm

# Create your views here.

@require_http_methods(["GET"])
@logged_in_user_only()
def index_reviews(request: WSGIRequest, pk: int):
    service = CertainReviewPageService()
    service.execute(pk)

    if service.is_error:
        return HttpResponseServerError('500')

    else:
        response = service.response.as_one_dictionary()
    
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
    service = AllReviewsPageSerive()
    service.execute()

    if service.is_error:
        status = 'error'
    else:
        status = 'success'
        
    return render(
        request, 
        'reviews/all_reviews.html', 
        context={
            'data': service.response.as_one_dictionary()['data'], 
            'status': status, 'title': 'PRO Reviews', 'PRO': True})


@require_http_methods(["POST"])
@logged_in_user_only()
def post_user_review(request: WSGIRequest):
    form = UserReviewForm(data=request.POST, files=request.FILES)

    if not form.is_valid():
        return JsonResponse({'status': 'form_validation_error', 'info': f'{form.errors.as_json()}'})
    
    else:
        service = CreateUserReviewService()
        service.execute(_id=user_id(request), data=form.clean())

        if service.is_error:

            if service.errors.type_of_server:
                return JsonResponse({'status': 'error', 'info': f'{service.errors.as_json()}'})
            return JsonResponse({'status': 'message', 'info': f'{service.errors.as_json()}'})
        
        return JsonResponse({'status': 'success', 'data': f'{service.response.as_json()}', 'flag': 'potato'})


@require_http_methods(["GET"])
@logged_in_user_only()
def all_users_reviews(request: WSGIRequest):
    service = AllUsersReviewsPageService()
    service.execute()

    if service.is_error:
        status = 'error'
    else:
        status = 'success'
        
    return render(request, 'reviews/all_reviews.html', 
    context={'data': service.response.as_one_dictionary()['data'], 'status': status, 'title': 'Amateur Reviews'})


@require_http_methods(["GET"])
@logged_in_user_only()
def index_user_reviews(request: WSGIRequest, pk: int):
    service = CertainUserReviewPageService()
    service.execute(pk)

    if service.is_error:
        return HttpResponseServerError('500')
    else:
        response = service.response.as_one_dictionary()

        data = response['data']
        next_id = response['next_id']
        prev_id = response['prev_id']
        nickname = response['author_nickname']

        return render(
            request, 'reviews/review.html', 
            context={'data': data, 
                'additional_info': {'next_id': next_id, 'prev_id': prev_id, 'nickname': nickname}})


@require_http_methods(["GET"])
@logged_in_user_only()
def is_user_like_it(request: WSGIRequest, pk: int):
    service = DoUserLikeReviewWithId()
    service.execute(_id=user_id(request), _rv_id=pk)

    if service.is_error:
        return JsonResponse({'status': 'error', 'info': f'{service.errors.as_json()}'})
    else:
        return JsonResponse({'status': 'success', 'data': f'{service.response.as_json()}'})


@require_http_methods(["GET"])
@logged_in_user_only()
def like_or_unlike_it(request: WSGIRequest, pk: int):
    service = LikeOrUnlikeIt()
    service.execute(_id=user_id(request), _rv_id=pk)

    if service.is_error:
        return JsonResponse({'status': 'error', 'info': f'{service.errors.as_json()}'})
    else:
        return JsonResponse({'status': 'success'})
