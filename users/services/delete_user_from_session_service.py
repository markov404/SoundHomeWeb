
from django.core.handlers.wsgi import WSGIRequest
from users.services.interfaces.ICommand import ICommand
from users.components.authorisation import Authorisation

class DeleteUserFromSessionService(ICommand):

    def execute(self, request: WSGIRequest) -> None:
        auth = Authorisation()
        auth.logout(request)