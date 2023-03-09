
from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.index_page, name="index_page"),
    path('error/', view=views.error_page, name="error_page"),
]
