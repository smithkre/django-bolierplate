from .base import *

DEBUG = False

INSTALLED_APPS += []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'OPTIONS': {
            'charset': 'utf8'
        },
    }
}

