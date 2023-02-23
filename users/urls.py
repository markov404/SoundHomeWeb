
from django.contrib.auth import urls
from django.urls import path, include

from . import views

urlpatterns = [
    path('authenticate/', view=views.auth, name="authentication_view"),
]
