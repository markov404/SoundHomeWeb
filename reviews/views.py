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
def index_reviews(request: WSGIRequest): 
    data = ReviewsPage().get_all_reviews_data()
    return render(request, 'reviews/reviews.html', context={'data': data[0]})
