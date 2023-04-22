
from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from django.views.decorators.http import require_http_methods
from utils.wrappers import not_logged_in_user_only

# Create your views here.


@not_logged_in_user_only()
def index_page(request: WSGIRequest):
    return render(request, 'common_app/index.html')


@require_http_methods(["GET"])
def error_page(request: WSGIRequest):
    try:
        code = request.GET['code']
        message = request.GET['message']
    except BaseException:
        code = 500

    return render(
        request,
        'common_app/error.html',
        context={
            'code': code,
            'message': message})
