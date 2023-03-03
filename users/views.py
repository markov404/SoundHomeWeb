
from django.http import HttpResponse

from django.shortcuts import redirect
from django.core.handlers.wsgi import WSGIRequest
from django.views.decorators.http import require_http_methods

from utils.wrappers import not_logged_in_user_only, logged_in_user_only

from users.services.delete_user_from_session_service import DeleteUserFromSessionService
from users.services.authenticate_and_auth_or_registr_user import AuthenticateAndAuthOrRegistrUser

# Create your views here.

@require_http_methods(["POST"])
@not_logged_in_user_only()
def auth(request: WSGIRequest):
    response = AuthenticateAndAuthOrRegistrUser().execute(request)
    if not isinstance(response, dict):
        return HttpResponse()
    
    if response['status'] == 'success':
        return redirect("profile_page")
    else:
        return HttpResponse(response['message'])

@require_http_methods(["GET"])
@logged_in_user_only()
def logout(request: WSGIRequest):
    DeleteUserFromSessionService().execute(request)
    return redirect("index_page")
