
from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>', view=views.index_reviews, name="ceraint_review"),
    path('all/', view=views.all_reviews, name="all_reviews"),
    path('post_user_review/', view=views.post_user_review, name="post_user_review"),
    path('all_users_review/', view=views.all_users_reviews, name="all_users_reviews"),
    path('amateur/<int:pk>', view=views.index_user_reviews, name="ceraint_user_review"),

    path('do_you_like_user_review/<int:pk>', view=views.is_user_like_it, name="is_user_like_it_review"),
    path('like_or_unlike_user_review/<int:pk>', view=views.like_or_unlike_it, name="like_or_unlike_user_review"),
]