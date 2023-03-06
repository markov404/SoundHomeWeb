
from django.shortcuts import redirect, render, HttpResponse
from django.http import JsonResponse
from django.core.handlers.wsgi import WSGIRequest
from django.views.decorators.http import require_http_methods

from utils.wrappers import not_logged_in_user_only, logged_in_user_only, active_user_only, non_active_user_only
from utils.sesssion import user_id

from users.services.delete_user_from_session_service import DeleteUserFromSessionService
from users.services.authenticate_and_auth_or_registr_user import AuthenticateAndAuthOrRegistrUser
from users.services.user_data_service import UserBasicDataService
from users.services.set_up_profile_service import SetUpProfileService


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


@logged_in_user_only()
@active_user_only()
def profile_page(request: WSGIRequest):
    response = UserBasicDataService().execute(user_id(request))
    if response['status'] == 'error':
        return HttpResponse('baad')

    return render(request, 'users/profile.html', context=response['data'])


@logged_in_user_only()
@non_active_user_only()
def set_up_profile(request: WSGIRequest):
    if request.method == "POST":
        response = SetUpProfileService().execute(request, user_id(request))
        return JsonResponse(response)
    elif request.method == "GET":
        pass
    
    return render(request, 'users/set_up_profile.html', context={})


@logged_in_user_only()
@active_user_only()
def change_user_ava(request: WSGIRequest):
    return JsonResponse('HUIAHUHUHU')


@logged_in_user_only()
@active_user_only()
def change_user_nickname(request: WSGIRequest):
    return JsonResponse('meme')
