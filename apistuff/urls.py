
from django.urls import path
from . import views

urlpatterns = [
    path('current_token', view=views.current_token),
    path('logs', view=views.get_warnings_logs),
]
