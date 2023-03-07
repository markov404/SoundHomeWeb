
from reviews.services.interfaces.ICommand import ICommand
from reviews.components.database_requests import get_all_users_review_data_list, get_user_nickname_by_pk

class AllUsersReviewsPageService(ICommand):
    def execute(self):
        data = self._extract_all_reviews()        
        data = self._define_author_of_reviews(data)

        return data

    def _extract_all_reviews(self) -> list[dict]:
        return get_all_users_review_data_list()

    def _define_author_of_reviews(self, data: list[str]) -> list[str]:
        
        for rev in data:
            usr_id = rev['user_id']
            nick = get_user_nickname_by_pk(usr_id)
            rev['nickname'] = nick
        
        return data

