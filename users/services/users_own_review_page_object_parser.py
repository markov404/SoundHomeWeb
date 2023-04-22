from django.core.paginator import Page
from utils.abstractions.abstract_classes.abs_services import BaseService


class UsersReviewPageObjectParser(BaseService):

    def execute(self, page_obj: Page) -> None:
        try:
            if page_obj.has_other_pages():
                self._extract_next_page(page_obj)
                self._extract_previous_page(page_obj)
            self._extract_objects_list(page_obj)
        except Exception as E:
            self.errors.append(f'{E}')

    def _extract_previous_page(self, page_obj: Page) -> None:
        if page_obj.has_previous():
            self._got_entities.append(
                {'previous_page': page_obj.previous_page_number()})
            return
        self._got_entities.append(
            {'previous_page': page_obj.paginator.num_pages})

    def _extract_next_page(self, page_obj: Page) -> None:
        if page_obj.has_next():
            self._got_entities.append(
                {'next_page': page_obj.next_page_number()})
            return
        self._got_entities.append({'next_page': 1})

    def _extract_objects_list(self, page_obj: Page) -> None:
        self._got_entities.append({'revs': page_obj.object_list})
