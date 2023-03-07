
from django.core.handlers.wsgi import WSGIRequest

from utils.abstractions.abstract_classes.abs_validators import ImageValidator
from reviews.services.interfaces.ICommand import ICommand
from reviews.components.validators import (
    ReviewTitleValidator,
    ReviewAlbumAuthorValidator,
    ReviewContentValidator)
from reviews.components.database_requests import create_user_review

class CreateUserReviewService(ICommand):
    
    def execute(self, _id: int, request: WSGIRequest):
        data = self._extract_all_data(request)
        if data is None:
            return {'status': 'error', 'message': 'Not enough data'}
        
        print(type(data['album_cover']))

        st1 = ImageValidator().is_valid(data['album_cover'])
        st2 = ReviewTitleValidator().is_valid(data['review_header'])
        st3 = ReviewAlbumAuthorValidator().is_valid(data['album_author'])
        st4 = ReviewContentValidator().is_valid(data['review_text'])
        data['review_score'] = float(data['review_score'])

        if not (st1 and st2 and st3 and st4):
            return {
                'status': 'error', 
                'message': 'Not valid data', 
                'concrete': f'Is image cool: {st1}, Is title cool: {st2}, Is author cool: {st3}, Is content cool: {st4}'}
        
        try:
            _new_review_id = self._make_user_review(data=data, _id=_id)
        except:
            return {'status': 'error', 'message': 'error in database'}
        else:
            return {'status': 'success', 'review_id': _new_review_id}

    def _extract_all_data(self, request: WSGIRequest) -> dict | None:
        
        try:
            output = dict()

            output['album_author'] = request.POST.get('album_author')
            output['album_title'] = request.POST.get('album_title')
            output['review_header'] = request.POST.get('review_header')
            output['review_text'] = request.POST.get('review_text')

            output['album_cover'] = request.FILES.get('album_cover')
            output['review_score'] = request.POST.get('review_score')
        except:
            output = None

        print(output)

        for item in output.items():
            if item[0] is None:
                output = None
                break
            
        return output

    def _make_user_review(self, data: dict, _id: int) -> None:
        return create_user_review(pk=_id, data=data)
