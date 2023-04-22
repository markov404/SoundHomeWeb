
from functools import wraps
from django.shortcuts import redirect
from django.http import HttpResponseServerError
from users.services.user_active_data_service import UserActiveDataService


def not_logged_in_user_only():

    def decorator(func):
        @wraps(func)
        def inner(request, *args, **kwargs):
            if 'member_id' in request.session:
                response = redirect("profile_page")
                return response
            return func(request, *args, **kwargs)

        return inner

    return decorator


def logged_in_user_only():

    def decorator(func):
        @wraps(func)
        def inner(request, *args, **kwargs):
            if 'member_id' not in request.session:
                response = redirect("index_page")
                return response
            return func(request, *args, **kwargs)

        return inner

    return decorator


def active_user_only():

    def decorator(func):
        @wraps(func)
        def inner(request, *args, **kwargs):
            _id = request.session['member_id']
            service = UserActiveDataService()
            service.execute(_id=_id)

            if service.is_error:
                return HttpResponseServerError('Error - 500')
            else:
                status = service.response[0]['active']

            if not status:
                response = redirect("profile_set_up_page")
                return response
            return func(request, *args, **kwargs)

        return inner

    return decorator


def non_active_user_only():

    def decorator(func):
        @wraps(func)
        def inner(request, *args, **kwargs):
            _id = request.session['member_id']
            service = UserActiveDataService()
            service.execute(_id=_id)

            if service.is_error:
                return HttpResponseServerError('Error - 500')

            else:
                status = service.response[0]['active']
            if status:

                response = redirect("profile_page")
                return response

            return func(request, *args, **kwargs)

        return inner

    return decorator
