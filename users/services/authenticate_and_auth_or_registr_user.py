from django.core.handlers.wsgi import WSGIRequest

from users.services.interfaces.ICommand import ICommand
from users.components.authentification import Authentification
from users.components.authorisation import Authorisation
from users.components.registration import Registration


class AuthenticateAndAuthOrRegistrUser(ICommand):

    def execute(self, req: WSGIRequest) -> dict:
        data = self._extract_email_and_passw(req) 
        if data is None:
            return {"status": "error", "message": "Invalid request"}
        
        email = data['email']
        password = data['password']

        what_to_do = self._choose_option(email, password)
        if what_to_do['status'] == 'error':
            return what_to_do

        match what_to_do['op_type']:
            case 'reg':
                self._registrate(req, email, password)
                return {'status': 'success', 'message': 'registred'}
            case 'auth':
                self._authorise(req, what_to_do['data'])
                return {'status': 'success', 'message': 'authorised'}


    def _extract_email_and_passw(self, request: WSGIRequest) -> dict | None:
        
        try:
            email = request.POST.get("email")
            password = request.POST.get("password")
        except:
            output = None
        else:
            output = {'email': email, 'password': password}

        return output
    
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
