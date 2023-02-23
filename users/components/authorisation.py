
from django.core.handlers.wsgi import WSGIRequest

class Authorisation:
    def login(self, request: WSGIRequest, pk_of_user: str):
        request.session['member_id'] = pk_of_user
        return request

    def logout(self, request: WSGIRequest):
        try:
            del request.session['member_id']
        except KeyError:
            pass

        return request