
from functools import wraps
from django.http import HttpResponse

def logged_in_user_only():

    def decorator(func):
        @wraps(func)
        def inner(request, *args, **kwargs):
            if 'member_id' in request.session:
                response = HttpResponse("Ты итак уже залогинен")
                return response
            return func(request, *args, **kwargs)

        return inner

    return decorator