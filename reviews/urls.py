

from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:pk>', view=views.index_reviews, name="ceraint_review"),
    path('all/', view=views.all_reviews, name="all_reviews"),
    path('update/', view=views.update, name='update')
]
