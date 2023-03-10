from django.shortcuts import redirect, render
from django.http import JsonResponse, HttpResponseServerError
from django.core.handlers.wsgi import WSGIRequest
from django.views.decorators.http import require_http_methods

from utils.wrappers import not_logged_in_user_only, logged_in_user_only, active_user_only, non_active_user_only
from utils.sesssion import user_id

from users.services.delete_user_from_session_service import DeleteUserFromSessionService
from users.services.authenticate_and_auth_or_registr_user import AuthenticateAndAuthOrRegistrUser
from users.services.user_data_service import UserBasicDataService
from users.services.set_up_profile_service import SetUpProfileService
from users.services.change_user_ava_service import ChangeUserAvaService
from users.services.change_user_nickname_service import ChangeUserNicknameService

from users.serializers import UserAdditionalInfoForm
from users.serializers import ChangeUserImageForm
from users.serializers import ChangeUserNicknameForm
from users.serializers import UserAARForm


# Create your views here.


@require_http_methods(["POST"])
@not_logged_in_user_only()
def auth(request: WSGIRequest):
    form = UserAARForm(data=request.POST)
    
    if not form.is_valid():
        return JsonResponse({'status': 'form_validation_error', 'info': f'{form.errors.as_json()}'})

    else:
        service = AuthenticateAndAuthOrRegistrUser()
        service.execute(req=request, data=form.clean())

        if service.is_error:
            if service.errors.type_of_server:
                return JsonResponse({'status': 'error', 'info': f'{service.errors.as_json()}'})
            
            return JsonResponse({'status': 'message', 'info': f'{service.errors.as_json()}'})
        
        return JsonResponse({'status': 'success'})


@require_http_methods(["GET"])
@logged_in_user_only()
def logout(request: WSGIRequest):
    service = DeleteUserFromSessionService()
    service.execute(request=request)

    if service.is_error:
        return HttpResponseServerError('500')
        
    return redirect("index_page")


@require_http_methods(["GET"])
@logged_in_user_only()
@active_user_only()
def profile_page(request: WSGIRequest):    
    service = UserBasicDataService()
    service.execute(_id=user_id(request))

    if service.is_error:
        return HttpResponseServerError(service.errors.as_messages())
    else:
        return render(request, 'users/profile.html', context=service.response.as_one_dictionary())


@require_http_methods(["POST", "GET"])
@logged_in_user_only()
@non_active_user_only()
def set_up_profile(request: WSGIRequest):
    if request.method == "POST":
        form = UserAdditionalInfoForm(data=request.POST, files=request.FILES)
        if not form.is_valid():
            return JsonResponse(
                {'status': 'form_validation_error', 
                'info': f'{form.errors.as_json()}'})

        else:
            service = SetUpProfileService()
            service.execute(data=form.clean(), _id=user_id(request))
            
            if service.is_error:
                if service.errors.type_of_server:
                    return JsonResponse({'status': 'error', 'info': f'{service.errors.as_json()}'})

                return JsonResponse({'status': 'message', 'info': f'{service.errors.as_json()}'})     
            
            return JsonResponse({'status': 'success'})
    elif request.method == "GET":
        pass
    
    return render(request, 'users/set_up_profile.html', context={})


@require_http_methods(["POST"])
@logged_in_user_only()
@active_user_only()
def change_user_ava(request: WSGIRequest):
    form = ChangeUserImageForm(files=request.FILES)

    if not form.is_valid():
        return JsonResponse({'status': 'form_validation_error', 'info': f'{form.errors.as_json()}'})

    else:
        service = ChangeUserAvaService()
        service.execute(data=form.clean(), _id=user_id(request))

        if service.is_error:
            if service.errors.type_of_server:
                return JsonResponse({'status': 'error', 'info': f'{service.errors.as_json()}'})

            return JsonResponse({'status': 'message', 'info': f'{service.errors.as_json()}'})

        return JsonResponse({'status': 'success'})


@require_http_methods(["POST"])
@logged_in_user_only()
@active_user_only()
def change_user_nickname(request: WSGIRequest):
    form = ChangeUserNicknameForm(data=request.POST)

    if not form.is_valid():
        return JsonResponse({'status': 'form_validation_error', 'info': f'{form.errors.as_json()}'})
        
    else:
        service = ChangeUserNicknameService()
        service.execute(data=form.clean(), _id=user_id(request))

        if service.is_error:
            if service.errors.type_of_server:
                return JsonResponse({'status': 'error', 'info': f'{service.errors.as_json()}'})

            return JsonResponse({'status': 'message', 'info': f'{service.errors.as_json()}'})
        
        return JsonResponse({'status': 'success'})
