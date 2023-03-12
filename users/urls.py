
from django.urls import path
from . import views

urlpatterns = [
    path('logout/', view=views.logout, name="logout_view"),
    path('authenticate/', view=views.auth, name="authentication_view"),
    path('profile/', view=views.profile_page, name="profile_page"),
    path('set_up_profile/', view=views.set_up_profile, name="profile_set_up_page"),
    path('set_up_profile/change_image', view=views.change_user_ava, name="chng_usr_image"),
    path('set_up_profile/change_nickname', view=views.change_user_nickname, name="chng_usr_nickname"),
    
    path('profile/user_review_listing/', view=views.user_reviews_listing, name="user_review_listing"),
    path('profile/favourite_review_listing/', view=views.fav_user_reviews, name="favourite_review_listing"),
]
