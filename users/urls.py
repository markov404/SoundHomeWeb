
from django.contrib.auth import urls
from django.urls import path, include

from . import views

urlpatterns = [
    path('logout/', view=views.logout, name="logout_view"),
    path('authenticate/', view=views.auth, name="authentication_view"),
]
