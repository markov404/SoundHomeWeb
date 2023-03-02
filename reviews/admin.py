from django.contrib import admin
from .models import Review, ReviewAudio, ReviewTranslation

# Register your models here.

admin.site.register(Review)
admin.site.register(ReviewAudio)
admin.site.register(ReviewTranslation)
