from .base import *

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'back-to-back-local',
        'USER': '',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    }
}

INSTALLED_APPS += (
    'debug_toolbar',
)

MIDDLEWARE_CLASSES += ['debug_toolbar.middleware.DebugToolbarMiddleware']

STATIC_ROOT = BASE_DIR.child("static")

STATICFILES_DIRS = (
    BASE_DIR.child('static_source'),
)

MEDIA_ROOT = BASE_DIR.child('media')
MEDIA_URL = '/media/'
