from .base import *

DEBUG = True

ALLOWED_HOSTS = []



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'nuevo_blog', 
        'USER':'postgres', 
        'PASSWORD':'root', 
        'HOST':'localhost', 
        'PORT':'',
    },
}
