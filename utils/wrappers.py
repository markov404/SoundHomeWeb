
from functools import wraps
from django.shortcuts import redirect
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
            status = UserActiveDataService().execute(_id)
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
            status = UserActiveDataService().execute(_id)
            if status:
                response = redirect("profile_page")
                return response
            return func(request, *args, **kwargs)

        return inner

    return decorator