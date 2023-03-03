
from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from utils.wrappers import not_logged_in_user_only

# Create your views here.


@not_logged_in_user_only()
def index_page(request: WSGIRequest):
    return render(request, 'common_app/index.html')
