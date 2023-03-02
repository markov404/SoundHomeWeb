
from __future__ import absolute_import, unicode_literals
from celery import shared_task

from reviews.services.update_reviews_in_db_service import UpdateReviewsInDBService

@shared_task
def UpdatingReviews():
    UpdateReviewsInDBService().execute()
