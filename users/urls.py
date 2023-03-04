
from django.urls import path
from . import views

urlpatterns = [
    path('logout/', view=views.logout, name="logout_view"),
    path('authenticate/', view=views.auth, name="authentication_view"),
    path('profile/', view=views.profile_page, name="profile_page"),
    path('set_up_profile/', view=views.set_up_profile, name="profile_set_up_page"),
]
