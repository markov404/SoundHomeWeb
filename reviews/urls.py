

from django.urls import path, include
from . import views

urlpatterns = [
    path('', view=views.index_reviews, name="index_reviews"),
]
