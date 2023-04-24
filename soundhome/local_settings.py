import os

# set debug level

DEBUG = True

# set allowed hosts

ALLOWED_HOSTS = ['127.0.0.1']

# set secret key

SECRET_KEY = 'oey*bt2+(#f7-r_%yr)pfft_e2%grtuqx+!38rc0w*t_ufbhn'

# set up databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}