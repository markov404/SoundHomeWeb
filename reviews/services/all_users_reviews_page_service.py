
from reviews.services.interfaces.ICommand import ICommand
from utils.abstractions.abstract_classes.abs_services import BaseService
from reviews.components.database_requests import get_all_users_review_data_list, get_user_nickname_by_pk


class AllUsersReviewsPageService(BaseService):
    def execute(self):
        self._extract_all_reviews()
        self._define_author_of_reviews()

    def _extract_all_reviews(self) -> None:
        data = get_all_users_review_data_list()
        if self.get_error(data):
            self.errors.append('Problem with getting user reviews data')
            return
        self._got_entities.append({'data': data})

    def _define_author_of_reviews(self) -> None:
        if not self.is_error:
            data = self._got_entities.pop()['data']

            if data is not None:
                for rev in data:
                    usr_id = rev['user_id']
                    nick = get_user_nickname_by_pk(usr_id)
                    if self.get_error(nick):
                        self.errors.append(
                            'Problem with getting user review author nickname')
                        return
                    rev['nickname'] = nick

                self._got_entities.append({'data': data})
            else:
                self.errors.append('There is no any user reviews yet!')
