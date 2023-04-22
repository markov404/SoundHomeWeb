
from django.core.handlers.wsgi import WSGIRequest


def is_logged_in(request: WSGIRequest):
    if 'member_id' in request.session:
        return {'member': request.session['member_id']}
    else:
        return {}
