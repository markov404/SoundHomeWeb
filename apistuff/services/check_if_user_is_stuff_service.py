import base64
from utils.abstractions.abstract_classes.abs_services import BaseService
from apistuff.components.database_requests import check_if_stuff_with_this_credentials_exists
from logging import getLogger

log = getLogger(__name__)


class CheckIfUserIsStuffService(BaseService):
    MANDATORY_FIELDS = {'username', 'password'}

    def execute(self, data: dict) -> None:
        super().execute(data)
        if self.is_error:
            return
        
        self._encrypt_all_data(data)
        self._find_target_stuff(data)

    def _encrypt_all_data(self, data: dict) -> None:
        try:
            for key in data.keys():
                data[key] = base64.b64decode(data[key]).decode()
        except Exception as E:
            log.warning(f'{E}')
            self.errors.append('Invalid type of encoding', 400)
    
    def _find_target_stuff(self, data):
        db_response = check_if_stuff_with_this_credentials_exists(
            username=data['username'],
            password=data['password']
        )

        if self.get_error(db_response):
            self.errors.append('Something goes wrong at the server side', 500)
            return
        
        if db_response == None:
            self.errors.append('Invalid credentials!', 400)
            return

        self.response.append({'user': db_response})
