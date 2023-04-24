
from django.urls import path
from . import views

urlpatterns = [
    path('current_token', view=views.current_token),
]
