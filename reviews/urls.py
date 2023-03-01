
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('<int:pk>', view=views.index_reviews, name="ceraint_review"),
    path('all/', view=views.all_reviews, name="all_reviews"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)