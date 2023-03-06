
from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>', view=views.index_reviews, name="ceraint_review"),
    path('all/', view=views.all_reviews, name="all_reviews"),
    path('post_user_review/', view=views.post_user_review, name="post_user_review"),
]