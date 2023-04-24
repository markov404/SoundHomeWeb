from uuid import uuid4
from utils.abstractions.abstract_classes.abs_services import BaseService
from apistuff.components.database_requests import (
    update_stuff_token_by_stuff_id,
    get_all_existing_tokens)
from logging import getLogger

log = getLogger(__name__)


class UpdateStuffTokenService(BaseService):
    def execute(self, _id: int) -> None:
        new_token = self._generate_new_token()
        self._update_stuff_token(_id, new_token)

        if not self.is_error:
            self.response.append({'your_new_token': new_token})

    def _generate_new_token(self) -> str:
        tokens = get_all_existing_tokens()
        if self.get_error(tokens):
            self.errors.append('Server error!', 500)
            return
        
        rand_token = uuid4()
        while rand_token in tokens:
            rand_token = uuid4()
        
        return rand_token
    
    def _update_stuff_token(self, _id: int, token: str) -> None:
        db_response = update_stuff_token_by_stuff_id(
            _id=_id, token=token)

        if self.get_error(db_response):
            self.errors.append('Something goes wrong at the server side', 500)
            return
