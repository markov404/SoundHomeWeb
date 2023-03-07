from django.contrib import admin
from reviews.services.update_reviews_in_db_service import UpdateReviewsInDBService
from reviews.models import Review, ReviewAudio, ReviewTranslation, UserReview

# Register your models here.

admin.site.register(Review)
admin.site.register(ReviewAudio)
admin.site.register(ReviewTranslation)
admin.site.register(UserReview)
