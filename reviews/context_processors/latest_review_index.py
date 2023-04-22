
from django.core.handlers.wsgi import WSGIHandler
from reviews.services.mini_services import LatestReviewId


def latest_review_index(request: WSGIHandler):
    try:
        output = {'latest_review': LatestReviewId().execute()}
    except BaseException:
        output = {'latest_review': None}
    return output
