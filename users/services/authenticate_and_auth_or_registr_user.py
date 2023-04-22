from django.core.handlers.wsgi import WSGIRequest
from utils.abstractions.abstract_classes.abs_services import BaseService

from users.components.authentification import Authentification
from users.components.authorisation import Authorisation
from users.components.registration import Registration


class AuthenticateAndAuthOrRegistrUser(BaseService):
    MANDATORY_FIELDS = {'email', 'password'}

    def execute(self, req: WSGIRequest, data) -> dict:
        super().execute(data=data)

        email = data['email']
        password = data['password']

        what_to_do = self._choose_option(email, password)
        if what_to_do['status'] == 'error':
            self.errors.append(what_to_do['message'], 400)

        if not self.is_error:
            match what_to_do['op_type']:
                case 'reg':
                    self._registrate(req, email, password)
                case 'auth':
                    self._authorise(req, what_to_do['data'])

    def _choose_option(self, email: str, password: str) -> dict:
        authe = Authentification()
        user = authe.is_user_exists(email)

        if user is None:
            return {"status": "success", "op_type": "reg"}

        if not authe.is_password_right(user, password):
            return {"status": "error", "message": "Password is not right"}

        return {"status": "success", "op_type": "auth", "data": user}

    def _authorise(self, request: WSGIRequest, user: int):
        autho = Authorisation()
        autho.login(request, user)

        del autho

    def _registrate(self, request: WSGIRequest, email: str, password: str):
        registr = Registration()
        user = registr.create_user(email=email, password=password)

        autho = Authorisation()
        autho.login(request, user.id)

        del registr
        del autho
