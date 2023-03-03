
from django.core.handlers.wsgi import WSGIRequest
from users.services.interfaces.ICommand import ICommand
from users.components.authorisation import Authorisation

class DeleteUserFromSessionService(ICommand):

    def execute(self, request: WSGIRequest) -> None:
        return self._delete_user_from_session(request)
    
    def _delete_user_from_session(self, req: WSGIRequest) -> None:
        auth = Authorisation()
        auth.logout(req)