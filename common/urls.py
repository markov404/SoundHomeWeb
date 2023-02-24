
from django.urls import path

from . import views

urlpatterns = [
    path('', view=views.index_page, name="index_page"),
    path('reviews/', view=views.reviews_page, name="reviews_page"),
    path('profile/', view=views.profile_page, name="profile_page")
]

