
from functools import wraps
from django.http import HttpResponse
from django.shortcuts import redirect


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
