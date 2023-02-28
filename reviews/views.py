
from django.http import HttpResponse
from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from utils.wrappers import logged_in_user_only

from selenium.webdriver import Chrome
from .components.driver import SeleniumClient
from .components.pitchfork import PitchForkScruber
from .models import Review

from .components.reviews_page import ReviewsPage

# Create your views here.

@logged_in_user_only()
def index_reviews(request: WSGIRequest, pk: int): 
    data = ReviewsPage().get_review_by_id(pk)

    next_id = 0
    prev_id = 0
    last_id = ReviewsPage().get_latest_id()
    print(last_id)
    if data['id'] == last_id:
        next_id = 1
        prev_id = data['id'] - 1
    elif data['id'] == 1:
        next_id = data['id'] + 1
        prev_id = last_id
    else:
        next_id = data['id'] + 1
        prev_id = data['id'] - 1

    return render(request, 'reviews/review.html', context={'data': data, 'additional_info': {'next_id': next_id, 'prev_id': prev_id}})

@logged_in_user_only()
def all_reviews(request: WSGIRequest):
    data = ReviewsPage().get_all_reviews_data()

    return render(request, 'reviews/all_reviews.html', context={'data': data})
