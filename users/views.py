
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.core.handlers.wsgi import WSGIRequest

from .wrappers.wrappers import logged_in_user_only
from .components.authentification import Authentification
from .components.authorisation import Authorisation

# Create your views here.

@require_http_methods(["POST"])
@logged_in_user_only()
def auth(request: WSGIRequest):
    email = request.POST.get("email")
    password = request.POST.get("password")

    auth = Authentification()
    user = auth.is_user_exists(email)
    if user is not None:
        if auth.is_password_right(user, password):
            authorisation = Authorisation()
            authorisation.login(request, user)
            return HttpResponse("Ты залогинился")
        else:
            return HttpResponse("Не правильный пароль")
    else:
        return HttpResponse("Нет такого емайла")        
