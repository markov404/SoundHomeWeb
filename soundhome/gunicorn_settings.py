command = '/home/web/code/my_web_apps/env/bin/gunicorn'
pythonpath = '/home/www'
bind = '127.0.0.1:8001'
workers = 3
user = 'www'
limit_request_fields = 32000
limit_request_fields_size = 0
raw_env = 'DJANGO_SETTINGS_MODULE=soundhome.settings'
