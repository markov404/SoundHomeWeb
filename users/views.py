
from django.http import HttpResponse

from django.shortcuts import redirect
from django.core.handlers.wsgi import WSGIRequest
from django.views.decorators.http import require_http_methods

from utils.wrappers import not_logged_in_user_only, logged_in_user_only

from .components.authentification import Authentification
from .components.authorisation import Authorisation
from .components.registration import Registration

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

            return redirect("profile_page")
        else:
            return HttpResponse("Не правильный пароль")
    else:
        registr = Registration()
        user = registr.create_user(email=email, password=password)

        if user is not False:
            autho = Authorisation()
            autho.login(request, user.id)

            del authe
            del registr
            del autho

            return redirect("profile_page")

        return HttpResponse("Нет такого емайла")        


@require_http_methods(["GET"])
@logged_in_user_only()
def logout(request: WSGIRequest):
    autho = Authorisation()
    autho.logout(request)

    return redirect("index_page")
