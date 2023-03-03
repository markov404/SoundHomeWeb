
from django.urls import path
from . import views

urlpatterns = [
    path('logout/', view=views.logout, name="logout_view"),
    path('authenticate/', view=views.auth, name="authentication_view"),
    path('profile/', view=views.profile_page, name="profile_page"),
]
