from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse

from rest_framework.decorators import api_view, throttle_classes
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle

from apistuff.services.check_if_user_is_stuff_service import CheckIfUserIsStuffService
from apistuff.services.update_stuff_token_service import UpdateStuffTokenService

# Create your views here.


class OncePerDayUserUserThrottle(UserRateThrottle):
    rate = '1/day'


@api_view(['GET'])
@throttle_classes([OncePerDayUserUserThrottle])
def current_token(request: WSGIRequest) -> JsonResponse:
    """ Username and Password should be sended in base64 """
    service = CheckIfUserIsStuffService()
    service.execute(request.GET.dict())

    if service.is_error:
            if service.errors.type_of_server:
                return Response(
                    {'status': 'error', 'info': f'{service.errors.as_json()}'})

            return Response(
                {'status': 'message', 'info': f'{service.errors.as_json()}'})

    
    target_stuff_id = service.response.as_one_dictionary()['user']
    
    service = UpdateStuffTokenService()
    service.execute(target_stuff_id)

    if service.is_error:
            if service.errors.type_of_server:
                return Response(
                    {'status': 'error', 'info': f'{service.errors.as_json()}'})

            return Response(
                {'status': 'message', 'info': f'{service.errors.as_json()}'})
    
    return Response(
        {'status': 'success', 'info': service.response.as_one_dictionary()}
    )


@api_view(['POST'])
def get_warnings_logs(request: WSGIRequest) -> JsonResponse:
    """ uuid4 code should be sent in headers """
    pass
