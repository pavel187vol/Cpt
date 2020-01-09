from .base import *

DEBUG = False

ADMINS = (
    ('Pavel V', 'pavel.voloscovich@gmail.com'),
)

ALLOWED_HOSTS = ['*']

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': 'crp',
       'USER': 'rood',
       'PASSWORD': 'zhelezo',
       'HOST' : '127.0.0.1',
       'PORT' : '5432',
   }
}
