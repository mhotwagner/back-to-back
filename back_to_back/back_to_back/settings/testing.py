from .base import *

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'back-to-back-testing',
        'USER': '',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    }
}

MEDIA_ROOT = BASE_DIR.child('media')
MEDIA_URL = '/media/'

STATIC_ROOT = BASE_DIR.child("static")
