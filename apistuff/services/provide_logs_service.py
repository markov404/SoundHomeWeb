from django.conf import settings
from utils.abstractions.abstract_classes.abs_services import BaseService
from apistuff.components.provide_logs import LogProvider
from apistuff.components.database_requests import get_all_existing_tokens

from logging import getLogger

log = getLogger(__name__)


class ProvideLogsService(BaseService):
    MANDATORY_FIELDS = {'token', 'type'}

    LOG_PATHS = {
        'warning': f'{settings.BASE_DIR}/warning.log',
        'access': f'{settings.BASE_DIR}/gunicorn.access.log',
        'error': f'{settings.BASE_DIR}/gunicorn.errors.log'
    }

    def execute(self, data) -> None:
        super().execute(data)
        if self.is_error:
            return
        
        type = data['type']
        if type not in self.LOG_PATHS.keys():
            self.errors.append('Not right type parameter!', 400)
            return

        path = self.LOG_PATHS[type]
        token = data['token']
        self._check_if_user_have_permission(token)

        if not self.is_error:
            self._provide_logs(path)

    def _check_if_user_have_permission(self, token: str) -> None:
        tokens = get_all_existing_tokens()
        if self.get_error(tokens):
            self.errors.append('Server error!', 500)
            return
        
        if token not in tokens:
            self.errors.append('Your token is not correct!', 400)
        
    
    def _provide_logs(self, path: str) -> None:
        provider = LogProvider()
        data = provider.read_logs(path=path)

        if self.get_error(data):
            self.errors.append(data['message'], data['code'])
            return
            
        self.response.append({'logs': data})
