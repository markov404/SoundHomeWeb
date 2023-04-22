from django.core.handlers.wsgi import WSGIRequest


def user_id(request: WSGIRequest) -> None | int:
    if 'member_id' in request.session:
        return request.session['member_id']
    else:
        return None
