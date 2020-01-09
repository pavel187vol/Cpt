from .base import *

DEBUG = False

ADMINS = (
    ('Pavel V', 'pavel.voloscovich@gmail.com'),
)

ALLOWED_HOSTS = ['*']

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': 'crp1',
       'USER': 'rood188',
       'PASSWORD': 'zhelezo187',
   }
}
