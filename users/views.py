
from django.http import HttpResponse
from django.core.handlers.wsgi import WSGIRequest
from django.views.decorators.http import require_http_methods

from .wrappers.wrappers import not_logged_in_user_only
from .components.authentification import Authentification
from .components.authorisation import Authorisation

# Create your views here.

@require_http_methods(["POST"])
@not_logged_in_user_only()
def auth(request: WSGIRequest):
    email = request.POST.get("email")
    password = request.POST.get("password")

    authe = Authentification()
    user = authe.is_user_exists(email)

    if user is not None:
        if authe.is_password_right(user, password):
            autho = Authorisation()
            autho.login(request, user)

            del authe
            del autho

            return HttpResponse("Ты залогинился")
        else:
            return HttpResponse("Не правильный пароль")
    else:
        return HttpResponse("Нет такого емайла")        
