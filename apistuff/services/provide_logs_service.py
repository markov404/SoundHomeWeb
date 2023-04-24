from django.conf import settings
from utils.abstractions.abstract_classes.abs_services import BaseService
from apistuff.components.provide_logs import LogProvider
from apistuff.components.database_requests import get_all_existing_tokens

from logging import getLogger

log = getLogger(__name__)


class ProvideLogsService(BaseService):
    MANDATORY_FIELDS = {'token'}
    LOG_PATH =  f'{settings.BASE_DIR}/warning.log'

    def execute(self, data) -> None:
        super().execute(data)
        if self.is_error:
            return
        
        token = data['token']
        self._check_if_user_have_permission(token)

        if not self.is_error:
            self._provide_logs()

    def _check_if_user_have_permission(self, token: str) -> None:
        tokens = get_all_existing_tokens()
        if self.get_error(tokens):
            self.errors.append('Server error!', 500)
            return
        
        if token not in tokens:
            self.errors.append('Your token is not correct!', 400)
        
    
    def _provide_logs(self) -> None:
        provider = LogProvider()
        data = provider.read_logs(path=self.LOG_PATH)
        self.response.append({'logs': data})
