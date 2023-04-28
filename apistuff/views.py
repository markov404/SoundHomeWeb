from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse

from rest_framework.decorators import api_view, throttle_classes
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle

from apistuff.services.check_if_user_is_stuff_service import CheckIfUserIsStuffService
from apistuff.services.update_stuff_token_service import UpdateStuffTokenService
from apistuff.services.provide_logs_service import ProvideLogsService

# Create your views here.


class OncePerDayUserUserThrottle(UserRateThrottle):
    rate = '1/day'


@api_view(['GET'])
def current_token(request: WSGIRequest) -> JsonResponse:
    """ Username and Password should be sended in base64 """
    service = CheckIfUserIsStuffService()
    service.execute(request.GET.dict())

    if service.is_error:
            if service.errors.type_of_server:
                return Response(
                    {'status': 'error', 'info': service.errors.as_one_dictionary()})

            return Response(
                {'status': 'message', 'info': service.errors.as_one_dictionary()})
<<<<<<< HEAD
=======

>>>>>>> 8a42f184bbb3886fc31f703d583aa01cc99bceaf
    
    target_stuff_id = service.response.as_one_dictionary()['user']
    
    service = UpdateStuffTokenService()
    service.execute(target_stuff_id)

    if service.is_error:
            if service.errors.type_of_server:
                return Response(
                    {'status': 'error', 'info': service.errors.as_one_dictionary()})

            return Response(
                {'status': 'message', 'info': service.errors.as_one_dictionary()})
    
    return Response(
        {'status': 'success', 'info': service.response.as_one_dictionary()}
    )


@api_view(['POST'])
def get_warnings_logs(request: WSGIRequest) -> JsonResponse:
    """ uuid4 code should be sent in headers 
        :body:
            {
                'token': str,
                'type': ('warning', 'access', 'error')
            }
    """
    
    service = ProvideLogsService()
    service.execute(request.POST.dict())

    if service.is_error:
            if service.errors.type_of_server:
                return Response(
                    {'status': 'error', 'info': f'{service.errors.as_json()}'})

            return Response(
                {'status': 'message', 'info': f'{service.errors.as_json()}'})

    return Response(
        {'status': 'success', 'info': service.response.as_one_dictionary()}
    )
