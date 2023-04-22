
from django.core.handlers.wsgi import WSGIRequest
from users.components.authorisation import Authorisation
from utils.abstractions.abstract_classes.abs_services import BaseService


class DeleteUserFromSessionService(BaseService):

    def execute(self, request: WSGIRequest) -> None:
        return self._delete_user_from_session(request)

    def _delete_user_from_session(self, req: WSGIRequest) -> None:
        auth = Authorisation()
        auth.logout(req)
