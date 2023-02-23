
from django.urls import path

from . import views

urlpatterns = [
    path('', view=views.index_page, name="index_page"),
    path('profile/', view=views.profile_page, name="profile_page")
]

